import discord
from discord.ext import commands
import random
import json
import asyncpraw as praw

with open("creds.json", "r") as creds:
    data = json.load(creds)["creds"]
    client_id = data["client_id"]
    client_secret = data["client_secret"]
    username = data["username"]
    password = data["password"]


class Redditstuff(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            user_agent="thejambot",
        )

    @commands.command(brief="Get a random meme, image or post from a subreddit")
    async def reddit(self, ctx, subreddit):
        subreddit = await self.reddit.subreddit(subreddit)
        submissions = []

        async for submission in subreddit.hot(limit=125):
            if not submission.stickied:
                submissions.append(
                    {
                        "title": submission.title,
                        "link": submission.url,
                        "text": submission.selftext,
                    }
                )

        submission = random.choice(submissions)
        embed = discord.Embed(
            title=submission["title"], description=submission["text"], colour=0xFF4500
        )
        embed.set_image(url=submission["link"])
        await ctx.send(embed=embed)

    @commands.command(brief="CD skid time owo")
    async def skid(self, ctx):
        subreddit = await self.reddit.subreddit("cyberdiscovery")
        submissions = []

        async for submission in subreddit.hot(limit=125):
            if not submission.stickied:
                submissions.append(
                    {
                        "title": submission.title,
                        "link": submission.url,
                        "text": submission.selftext,
                    }
                )

        submission = random.choice(submissions)
        embed = discord.Embed(
            title=submission["title"], description=submission["text"], colour=0x0F1E33
        )  # change to cd blue
        embed.set_image(url=submission["link"])
        await ctx.send(embed=embed)

    @commands.command(brief="Get top answers for r/askreddit questions")
    async def askreddit(self, ctx):
        subreddit = await self.reddit.subreddit("AskReddit")
        submissions = []

        async for submission in subreddit.hot(limit=100):
            if not submission.stickied:
                submissions.append(submission)

        submission = random.choice(submissions)
        comments = await submission.comments()
        await comments.replace_more(limit=0)
        comment = random.choice(comments).body

        embed = discord.Embed(
            title=submission.title, description=comment, colour=0xFF4500
        )
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

    @commands.command(brief="Get top responses from Am I The Asshole Posts.")
    async def aita(self, ctx):
        subreddit = await self.reddit.subreddit("AmItheAsshole")
        submissions = []

        async for submission in subreddit.hot(limit=100):
            if not submission.stickied:
                submissions.append(submission)

        submission = random.choice(submissions)
        comments = await submission.comments()
        await comments.replace_more(limit=0)
        comment = random.choice(comments).body

        embed = discord.Embed(
            title=submission.title, description=comment, colour=0xFFA500
        )
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Redditstuff(client))
