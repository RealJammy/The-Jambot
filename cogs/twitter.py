import discord
from discord.ext import commands, tasks
import tweepy
from datetime import datetime, timedelta

#insert with own values (OAuth 2)
auth = tweepy.AppAuthHandler(key,secret) #insert own details
api = tweepy.API(auth)

accounts = ["jameslyne","CyberDiscUK"]

class Twitter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tweet(self, ctx):
        await ctx.send("Loading tweets in past day... (may not return results)")
        for account in accounts:
            for tweet in tweepy.Cursor(api.user_timeline, id=account).items():
                if tweet.created_at > (datetime.utcnow()-timedelta(hours=24)):
                    msg = f"@{account} (re)tweeted at {tweet.created_at}\nhttps://twitter.com/twitter/status/{tweet.id}"
                    await ctx.send(msg)
                else:
                    break

     # TODO: create background process to get tweets every hour
def setup(client):
    client.add_cog(Twitter(client))
