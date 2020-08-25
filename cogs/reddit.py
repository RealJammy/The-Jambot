import discord
from discord.ext import commands
import random
import json
import asyncpraw as praw

with open("../creds.json", "r") as creds:
	data = json.load(creds)["creds"]
	client_id = data["client_id"]
	client_secret = data["client_secret"]
	username = data["username"]
	password = data["password"]

class Redditstuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief="Get a random meme from a subreddit")
    async def reddit(self, ctx, subreddit):
        reddit = praw.Reddit(client_id = client_id, 
					client_secret = client_secret, 
					username = username, 
					password = password, 
					user_agent = "thejambot")
        
        subreddit = await reddit.subreddit(subreddit)
        submissions = []

        async for submission in subreddit.hot(limit = 100):
            if not submission.stickied:
                submissions.append({"title":submission.title, "link":submission.url, "text":submission.selftext})
        submission = random.choice(submissions)

        embed = discord.Embed(title=submission["title"], description=submission["text"])
        embed.set_image(url=submission["link"])
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Redditstuff(client))