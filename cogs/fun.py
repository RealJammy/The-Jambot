import discord
from discord.ext import commands

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #ADD FUN STUFF HERE

def setup(client):
    client.add_cog(fun(client))