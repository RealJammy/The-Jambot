import discord
from discord.ext import commands, tasks
from googletrans import Translator, constants
from pprint import pprint

class Translate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief="Translate from spanish to english!")
    async def spanglish(self, ctx, *, text):
        translator = Translator()
        translation = translator.translate(text)
        await ctx.message.delete()
        await ctx.send(translation.replace("@", ""))

def setup(client):
    client.add_cog(Translate(client))
