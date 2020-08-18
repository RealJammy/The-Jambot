import discord
from discord.ext import commands, tasks
import random
import requests
import json
from Crypto.Util.number import long_to_bytes

class useful(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(brief='Decode a number to bytes')
    async def lb(self, ctx, arg):
        try:
            await ctx.send(long_to_bytes(int(arg)).decode().replace("@",""))
        except:
            await ctx.send("Failed <:sex:736200562890113055>")

def setup(client):
    client.add_cog(useful(client))
