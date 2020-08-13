import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix = ';')

@client.command(brief = 'Reloads cog.', description = 'Do ";reload cog".')
@has_permissions(administrator = True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

    await ctx.send(f'"{extension}" reloaded')

for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')
#just doing client.load_extension for each cog also works- i just like this :p

client.run('')#api key here :)