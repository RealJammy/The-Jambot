import discord
from discord.ext import commands, tasks
from Crypto.Util.number import long_to_bytes

class Useful(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Decode a number to bytes.')
    async def lb(self, ctx, arg):
        try:
            await ctx.send(long_to_bytes(int(arg)).decode().replace("@",""))
        except:
            await ctx.send("Failed <:sex:736200562890113055>")

    @commands.command(brief='Gives a bot discord invite.')
    async def invite(self, ctx):
        await ctx.send('https://discord.com/api/oauth2/authorize?client_id=742802810843693089&permissions=8&scope=bot')
    
    @commands.command(brief='Gives a link to The Jambot repo.')
    async def repo(self, ctx):
        await ctx.send('https://github.com/RealJammy/The-Jambot')
        await ctx.send('pls star owo')

    @commands.command(brief='Displays this message!')
    async def help(self, ctx):
        cogs = self.client.cogs
        helpMessage = discord.Embed(title='Help', colour=discord.Colour.purple())
        for cog in cogs:
            commands = self.client.get_cog(cog).get_commands()
            text = '\n'.join([f'`{c.name}`: {c.brief} {c.description}' for c in commands])
            helpMessage.add_field(name=f'{cog}', value=text, inline=False)
            
        await ctx.send(embed=helpMessage)

def setup(client):
    client.add_cog(Useful(client))