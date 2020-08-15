import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix = '.')

@client.command(brief = 'Reloads cog.', description = 'Do ";reload cog".')
@has_permissions(administrator = True)
async def reload(ctx, extension):    
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'"{extension}" reloaded')

client.load_extension('cogs.fun')
client.load_extension('cogs.admin')
client.run('')#api key here :)
