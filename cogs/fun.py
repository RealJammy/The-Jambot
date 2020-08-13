import discord
from discord.ext import commands
import random

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #FUN

    @commands.command(brief='Random anime.')
    async def anime(self, ctx):
        image = discord.Embed()
        image.set_image(url=f'https://www.thiswaifudoesnotexist.net/example-{random.randint(0, 100000)}.jpg')
        await ctx.send(embed=image)

    @commands.command(brief='No anime.')
    async def noanime(self, ctx):
        await ctx.send('https://i.kym-cdn.com/entries/icons/original/000/027/108/anime.jpg')
    
    @commands.command(brief='Ping!')
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(commands.latency * 1000)}ms')

    @commands.command(brief='Lyne.')
    async def lyne(self, ctx):
        await ctx.send('http://www.risk-uk.com/wp-content/uploads/2015/04/JamesLyneSANSCyberAcademy1.png')

    @commands.command(brief='Github.')
    async def github(self, ctx):
        await ctx.send('https://github.com/RealJammy/The-Jambot/blob/master/README.md')

    @commands.command(brief='No leaking!!!')
    async def noleek(self, ctx):
        await ctx.send('https://game.joincyberdiscovery.com/assets/videos/cheating_message.mp4?version=4.2.0')

def setup(client):
    client.add_cog(fun(client))
