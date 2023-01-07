import discord
from discord.ext import commands
import random
import json
import aiohttp
from TextToOwO import owo

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
                "https://json.reddit.com/r/AnimeDrawings/hot/?sort=controversial",
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



    @commands.command(brief="random.")
    async def randomcmd(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=hr03xF08qoU")

    @commands.command(brief="Ping!")
    async def ping(self, ctx):
        await ctx.send(f"pong!\n{round(self.client.latency * 1000)}ms")

    @commands.command(aliases=['epicgamerate', 'egr', 'epicgr', 'egrate', 'epicgamerr8', 'epicgamer8'])
    async def epicgamerrate(self, ctx, member: discord.Member = None):
        num = random.randint(1, 100)
        if member is None:
            member = ctx.author

        membervar = member.display_name

        embed = discord.Embed(
            title=f"Epic Gamer Rate :sunglasses:",
            description=f"{membervar} is {num}% epic gamer."
        )
        embed.color = discord.Color.random()
        embed.set_footer(text="Gamers = Poggers")
        await ctx.send(embed=embed)

    @commands.command(aliases=['sr', 'simpr', 'srate', 'sr8'])
    async def simprate(self, ctx, member: discord.Member = None):
        num = random.randint(1, 100)
        if member is None:
            member = ctx.author

        membervar = member.display_name

        embed = discord.Embed(
            title=f"Simp Rate :blush:",
            description=f"{membervar} is {num}% simp."
        )
        embed.color = discord.Color.random()
        embed.set_footer(text="Their favourite show be the SIMPsons")
        await ctx.send(embed=embed)


    @commands.command(brief="Lyne.")
    async def lyne(self, ctx):
        await ctx.send(
            "http://www.risk-uk.com/wp-content/uploads/2015/04/JamesLyneSANSCyberAcademy1.png"
        )

    @commands.command(brief="Github.", aliases=['ghstats'])
    async def github(self, ctx):
        await ctx.send("https://github.com/RealJammy/The-Jambot/blob/master/README.md")

    @commands.command(brief="No leaking!!!")
    async def noleek(self, ctx):
        await ctx.send(
            "https://cdn.discordapp.com/attachments/509080315369881600/1035311851661181069/cheating_message.mp4"
        )



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

    @commands.command(brief="to ping spam chandos")
    async def elmi(self, ctx):
        await ctx.send("Hey <@573555023322021888> i was right")

    @commands.command(brief="To force JSnerd to get some sleep")
    async def jsnerd(self, ctx):
        user = self.client.get_user(624713824087572480)
        await user.send("aaaaaaaaaaaa go to sleep")

    @commands.command(brief="bean")
    async def bean(self, ctx):
        for i in range(100):
            userf = self.client.get_user(573555023322021888)
            await userf.send("the 1 pound is mine :3")



    @commands.command(brief="dm emily a dog pic")
    async def doggy(self, ctx):
        try:
            image = discord.Embed()
            async with self.session.get(
                "https://some-random-api.ml/img/dog"
            ) as resp:
                imageUrl = (await resp.json())["link"]
            image.set_image(url=imageUrl)
            await ctx.send("Doggo has been sent!")
            userb = self.client.get_user(509464597087125507)
            await userb.send(embed=image)
        except:
            await ctx.send("No doggo sent :(")

    @commands.command(brief="djungelskog sent to jam")
    async def skoggy(self, ctx):
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
            await ctx.send("Now to send one to jammy...")
            userc = self.client.get_user(448519423901433876)
            await userc.send(embed=image)
            await ctx.send("Sent!")
        except:
            await ctx.send("No djungelskog :(")

    @commands.command(brief="EHF Playlist- aka an elite playlist")
    async def ehftunez(self, ctx):
        await ctx.send(
            "https://open.spotify.com/playlist/5ATjDhDw84rid3SQ4rXNZ7?si=BX8GuJYXTXSo09T5ZlybdA"
        )
    @commands.command(brief="Sends a message as the bot.")
    @commands.has_permissions(administrator=True)
    async def send(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text)

    @commands.command(brief="owoify your messages!")
    async def owofier(self, ctx, *, text):
        var = owo.text_to_owo(text)
        await ctx.message.delete()
        await ctx.send(var.replace("@", ""))



    @commands.command(brief="Serves as a warning for making horrible code")
    async def jamcode(self, ctx):
        await ctx.send("your code is bad \n and you should feel bad for writing it")







def setup(client):
    client.add_cog(Fun(client))
