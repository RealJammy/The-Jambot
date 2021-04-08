import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import time
from yahoo-fin import * as si

class Stocks(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief="get the price of a stonk")
    async def stonkers(self, ctx, *, text):
        stonk = si.get_live_price(text)
        await ctx.send(f'The current price of {text} is {stonk}')

    @commands.command(brief="get the price of gme")
    async def moon(self, ctx, *, text):
        stonk = si.get_live_price("gme")
        await ctx.send(f'The current price of {text} is {stonk}')



def setup(client):
    client.add_cog(Stocks(client))
