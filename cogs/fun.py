import discord
from discord.ext import commands
import random
import json
import aiohttp


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    @commands.command(brief="Random waifu.")
    async def waifu(self, ctx):
        image = discord.Embed()
        image.set_image(
            url=f"https://www.thiswaifudoesnotexist.net/example-{random.randint(0, 100000)}.jpg"
        )
        await ctx.send(embed=image)

    @commands.command(brief="red panda!")
    async def panda(self, ctx):
        try:
            image = discord.Embed()
            async with self.session.get(
                "https://some-random-api.ml/img/red_panda"
            ) as resp:
                imageUrl = (await resp.json())["link"]
            image.set_image(url=imageUrl)
            await ctx.send(embed=image)
        except:
            await ctx.send("No panda :(")

    @commands.command(brief="random anime drawing")
    async def anime(self, ctx):
        try:
            async with self.session.get(
                "https://json.reddit.com/r/AnimeDrawings/hot/?sort=hot",
                headers={"User-Agent": "Mozilla/5.0"},
            ) as resp:
                data = (await resp.json())["data"]
            count = int(data["dist"])
            post = data["children"][random.randint(1, count)]["data"]
            image_url = post["url_overridden_by_dest"]
            title = post["title"]
            image = discord.Embed(title=title)
            image.set_image(url=image_url)
            await ctx.send(embed=image)
        except:
            await ctx.send("no anime")

    @commands.command(brief="random kirby!")
    async def kirb(self, ctx):
        try:
            async with self.session.get(
                "https://json.reddit.com/r/Kirby/hot/?sort=hot",
                headers={"User-Agent": "Mozilla/5.0"},
            ) as resp:
                data = (await resp.json())["data"]
            count = int(data["dist"])
            post = data["children"][random.randint(1, count)]["data"]
            image_url = post["url_overridden_by_dest"]
            title = post["title"]
            image = discord.Embed(title=title)
            image.set_image(url=image_url)
            await ctx.send(embed=image)
        except:
            await ctx.send("no kirb :c")

    @commands.command(brief="random meme")
    async def meme(self, ctx):
        try:
            async with self.session.get(
                "https://json.reddit.com/r/memes/hot/?sort=hot",
                headers={"User-Agent": "Mozilla/5.0"},
            ) as resp:
                data = (await resp.json())["data"]
            count = int(data["dist"])
            post = data["children"][random.randint(1, count)]["data"]
            image_url = post["url_overridden_by_dest"]
            title = post["title"]
            image = discord.Embed(title=title)
            image.set_image(url=image_url)
            await ctx.send(embed=image)
        except:
            await ctx.send("No meme :(")

    @commands.command(brief="shoob :)")
    async def shoob(self, ctx):
        try:
            image = discord.Embed()
            async with self.session.get(
                "https://dog.ceo/api/breed/samoyed/images/random"
            ) as resp:
                image_url = (await resp.json())["message"]
            image.set_image(url=image_url)
            await ctx.send(embed=image)
        except:
            await ctx.send("No shoob :(")

    @commands.command(brief="djungelskog!")
    async def djungelskog(self, ctx):
        try:
            async with self.session.get(
                "https://json.reddit.com/r/Djungelskog/hot/?sort=hot",
                headers={"User-Agent": "Mozilla/5.0"},
            ) as resp:
                data = (await resp.json())["data"]
            count = int(data["dist"])
            post = data["children"][random.randint(1, count)]["data"]
            image_url = post["url_overridden_by_dest"]
            title = post["title"]
            image = discord.Embed(title=title)
            image.set_image(url=image_url)
            await ctx.send(embed=image)
        except:
            await ctx.send("No djungelskog :(")

    @commands.command(brief="koala!")
    async def koala(self, ctx):
        try:
            image = discord.Embed()
            async with self.session.get("https://some-random-api.ml/img/koala") as resp:
                image_url = (await resp.json())["link"]
            image.set_image(url=image_url)
            await ctx.send(embed=image)
        except:
            await ctx.send("No koala :(")

    @commands.command(brief="No anime.")
    async def noanime(self, ctx):
        await ctx.send(
            "https://i.kym-cdn.com/entries/icons/original/000/027/108/anime.jpg"
        )

    @commands.command(brief="random.")
    async def randomcmd(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=63qtYi1nwcs")

    @commands.command(brief="Ping!")
    async def ping(self, ctx):
        await ctx.send(f"pong!\n{round(self.client.latency * 1000)}ms")

    @commands.command(brief="Lyne.")
    async def lyne(self, ctx):
        await ctx.send(
            "http://www.risk-uk.com/wp-content/uploads/2015/04/JamesLyneSANSCyberAcademy1.png"
        )

    @commands.command(brief="Github.")
    async def github(self, ctx):
        await ctx.send("https://github.com/RealJammy/The-Jambot/blob/master/README.md")

    @commands.command(brief="No leaking!!!")
    async def noleek(self, ctx):
        await ctx.send(
            "https://game.joincyberdiscovery.com/assets/videos/cheating_message.mp4?version=4.2.0"
        )

    @commands.command(brief="uwu")
    async def uwu(self, ctx):
        await ctx.send("uwu!")

    @commands.command(brief="owo")
    async def owo(self, ctx):
        await ctx.send("owo!")

    @commands.command(brief="yeet")
    async def yeet(self, ctx):
        await ctx.send("hi uwu :3")

    @commands.command(brief="scream! Only works on PC/ Desktop.")
    async def scream(self, ctx):
        await ctx.send("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", tts=True)

    @commands.command(brief="ping pig")
    async def pingpig(self, ctx, amount=1):
        message = await ctx.send("<@295440396006326272>")
        await ctx.channel.purge(limit=amount + 1)

    @commands.command(brief="Slough Song")
    async def slough(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=nwMK2ywRF78")

    @commands.command(brief="to nag rag")
    async def nagrag(self, ctx):
        await ctx.send("Hey <@624713824087572480> this is a nag")

    @commands.command(brief="to make das fuck off")
    async def fuckoffdas(self, ctx):
        await ctx.send("Hey <@695222074192429136> fuck off")

    @commands.command(brief="To force JSnerd to get some sleep")
    async def jsnerd(self, ctx):
        user = self.client.get_user(624713824087572480)
        await user.send("aaaaaaaaaaaa go to sleep")

    @commands.command(brief="To dm the creator of the bot a quick hello")
    async def hello(self, ctx):
        user = self.client.get_user(448519423901433876)
        await user.send("hewwoa!")

    @commands.command(brief="EHF Playlist- aka an elite playlist")
    async def ehftunez(self, ctx):
        await ctx.send(
            "https://open.spotify.com/playlist/5ATjDhDw84rid3SQ4rXNZ7?si=BX8GuJYXTXSo09T5ZlybdA"
        )


def setup(client):
    client.add_cog(Fun(client))
