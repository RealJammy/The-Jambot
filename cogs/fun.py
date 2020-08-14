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
        await ctx.send(f'pong!\n{round(self.client.latency * 1000)}ms')


    @commands.command(brief='Lyne.')
    async def lyne(self, ctx):
        await ctx.send('http://www.risk-uk.com/wp-content/uploads/2015/04/JamesLyneSANSCyberAcademy1.png')

    @commands.command(brief='Github.')
    async def github(self, ctx):
        await ctx.send('https://github.com/RealJammy/The-Jambot/blob/master/README.md')

    @commands.command(brief='No leaking!!!')
    async def noleek(self, ctx):
        await ctx.send('https://game.joincyberdiscovery.com/assets/videos/cheating_message.mp4?version=4.2.0')
        
    @commands.command(brief='uwu')
    async def uwu(self, ctx):
        await ctx.send('uwu!')

    @commands.command(brief='scream! Only works on PC/ Desktop.')
    async def scream(self, ctx):
        await ctx.send('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', tts=True)
        
    @commands.command(brief='Red Panda (awwww look how cute it is)')
    async def panda(self, ctx):
        await ctx.send('https://pbs.twimg.com/media/ELjqorWUEAEwuPc?format=jpg&name=small')
    
    
    @commands.command(brief='ping pig')
    async def pingpig(self, ctx, amount=1):
      message = await ctx.send('<@295440396006326272>')
      await ctx.channel.purge(limit=amount+1)
 

    @commands.command(brief='Slough Song')
    async def slough(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=nwMK2ywRF78')
            
    @commands.command(brief='to nag rag')
    async def nagrag(self, ctx):
        await ctx.send('Hey <@624713824087572480> this is a nag')

def setup(client):
    client.add_cog(fun(client))
