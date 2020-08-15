import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix = '.')

@client.command(brief = 'Reloads cog.', description = 'Do ";reload cog".')
@has_permissions(administrator = True)
async def reload(ctx, extension):
    if ctx.message.author.id == 448519423901433876:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Successfully reloaded "{extension}".')
    else:
        await ctx.send("You must be Jammy.")

client.load_extension('cogs.fun')
client.load_extension('cogs.admin')

client.run('NzQ0MzEyODA0OTY1ODc1OTA1.XzhZUQ.hyg8Ey3BUfRDquQ4EjPCh0H9yoE')#api key here :)