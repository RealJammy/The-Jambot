import discord
from discord.ext import commands
import random
import json
import asyncpraw as praw
import configparser

class fiftyfifty(commands.Cog):

    def __init__(self, client, sub, limit, order, time):
        config = configparser.ConfigParser()
        config.read('conf.ini')
        self.reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                                  client_secret=config['REDDIT']['client_secret'],
                                  user_agent='speccy')
        self.client = client


    @commands.command(brief="fiftyfifty HOT/TOP/NEW hour/day/month/week/year/all")
    async def fiftyfifty(self, ctx, order, time):       
        sub="fiftyfifty" 
        if order == 'hot':
            submissions = await self.reddit.subreddit(sub).hot(limit=100,time=time) #get hot
        elif order == 'top':
            submissions = await self.reddit.subreddit(sub).top(limit=100,time=time) #get top
        elif order == 'new':
            submissions = await self.reddit.subreddit(sub).new(limit=100,time=time) #get new

        choice = [] #empty list ye
        async for submission in submissions:
            if not submission.stickied:
                choice.append({"title":submission.title, "link":submission.url, "desc":submission.selftext}) #add it all to list

        chosen = random.choice(choice) #choose random one outta the lot

        embed = discord.Embed(title=chosen["title"], description=chosen["desc"])
        embed.set_image(url=chosen["link"]) #handles video n image 
        await ctx.send(embed=embed) #send embed

def setup(client):
    client.add_cog(fiftyfifty(client))
