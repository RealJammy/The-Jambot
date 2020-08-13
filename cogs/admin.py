import discord
from discord.ext import commands

class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #check if this works instead of going off of ur old code jamie
    async def on_ready(self):
        print('The Jambot is here. Hello.')
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Watching over skids'))

    @commands.Cog.listener()
    async def on_member_join(self, member): #also check if this works lol- will run one big test at the end probably
        channel = discord.utils.get(message.guild.channels, name='general')
        await channel.send(f'{member} has joined the server.')

    @commands.Cog.listener()
    async def on_member_remove(self, member): #should probably stop putting a note to check at every function lmao
        channel = discord.utils.get(message.guild.channels, name='general')
        await channel.send(f'{member} has left the server.')
    
    @commands.Cog.listener()
    async def on_commmand_error(self, ctx, error): 
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please give all the arguments.')
        print(f"ERROR: {error}")

def setup(client):
    client.add_cog(admin(client))