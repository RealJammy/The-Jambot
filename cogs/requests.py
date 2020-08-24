import discord
from discord.ext import commands, tasks
import random
import requests
import json
from Crypto.Util.number import long_to_bytes

class requests(commands.Cog):

    def __init__(self, client):
        self.client = client
        
     # commands that use requests
     
     
    @commands.command(brief='Random waifu.')
    async def waifu(self, ctx):
        image = discord.Embed()
        image.set_image(url=f'https://www.thiswaifudoesnotexist.net/example-{random.randint(0, 100000)}.jpg')
        await ctx.send(embed=image)
        
    @commands.command(brief='red panda!')
    async def panda(self, ctx):
        try:
            image = discord.Embed()
            imageUrl = json.loads(requests.get('https://some-random-api.ml/img/red_panda').text)['link']
            image.set_image(url=imageUrl)
            await ctx.send(embed=image)
        except:
            await ctx.send("No panda :(")
            
    @commands.command(brief='random anime drawing')
    async def anime(self, ctx):
        try:
            res = requests.get('https://json.reddit.com/r/AnimeDrawings/hot/?sort=hot', headers={'User-Agent': 'Mozilla/5.0'})
            data = json.loads(res.text)['data']
            count = int(data['dist'])
            post = data['children'][random.randint(1, count)]['data']
            imageUrl = post['url_overridden_by_dest']
            title = post['title']
            image = discord.Embed(title=title)
            image.set_image(url=imageUrl)
            await ctx.send(embed=image)
        except:
            await ctx.send('no anime')

    @commands.command(brief='random meme')
    async def meme(self, ctx):
        try:
            res = requests.get('https://json.reddit.com/r/memes/hot/?sort=hot', headers={'User-Agent': 'Mozilla/5.0'})
            data = json.loads(res.text)['data']
            count = int(data['dist'])
            post = data['children'][random.randint(1, count)]['data']
            imageUrl = post['url_overridden_by_dest']
            title = post['title']
            image = discord.Embed(title=title)
            image.set_image(url=imageUrl)
            await ctx.send(embed=image)
        except:
            await ctx.send('No meme :(')
    @commands.command(brief='shoob :)')
    async def shoob(self, ctx):
        try:
            image = discord.Embed()
            imageUrl = json.loads(requests.get('https://dog.ceo/api/breed/samoyed/images/random').text)['message']
            image.set_image(url=imageUrl)
            await ctx.send(embed=image)
        except:
            await ctx.send("No shoob :(")

    @commands.command(brief='djungelskog!')
    async def djungelskog(self, ctx):
        try:
            res = requests.get('https://json.reddit.com/r/Djungelskog/hot/?sort=hot', headers={'User-Agent': 'Mozilla/5.0'})
            data = json.loads(res.text)['data']
            count = int(data['dist'])
            post = data['children'][random.randint(1, count)]['data']
            imageUrl = post['url_overridden_by_dest']
            title = post['title']
            image = discord.Embed(title=title)
            image.set_image(url=imageUrl)
            await ctx.send(embed=image)
        except:
            await ctx.send('No djungelskog :(')


def setup(client):
    client.add_cog(requests(client))
