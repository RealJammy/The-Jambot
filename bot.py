# Code heavily refactored from RealJammy/The-Jambot

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import json
import BotMessages
import sys

# Loading variables from config
try:
    bmConsoleCfg = json.load(open("config/console", "r"))
    bmConsole = BotMessages.Console(bmConsoleCfg["activated"], bmConsoleCfg["member_joined"], bmConsoleCfg["member_left"], bmConsoleCfg["command_error"], bmConsoleCfg["cog_reload"])
    print("Console Config loaded")
except:
    bmConsole = BotMessages.Console()
    print("Console Config failed to load! Using defaults as specified in BotMessages.py")

try:
    bmGuildCfg = json.load(open("config/guild", "r"))
    bmGuild = BotMessages.Guild(bmGuildCfg["insufficient_perms"], bmGuildCfg["member_joined"], bmGuildCfg["member_left"], bmGuildCfg["command_error"], bmGuildCfg["cog_reload"])
    print("Guild Config loaded")
except:
    bmGuild = BotMessages.Guild()
    print("Guild Config failed to load")

try:
    bmMetaCfg = json.load(open("config/meta", "r"))
    bmMeta = BotMessages.Meta(bmMetaCfg["cmd_prefix"], bmMetaCfg["bot_game"], bmMetaCfg["admin_ids"])
    print("Meta config loaded")
except:
    bmMeta = BotMessages.Meta()
    print("Meta config failed to load")

try:
    credsCfg = json.load(open("config/creds", "r"))
    botToken = credsCfg["bot_token"]
    print("Creds loaded")
except: 
    print("Creds failed to load! Fatal error, exiting")
    exit()

client = commands.Bot(command_prefix = bmMeta.cmd_prefix)

@client.event
async def on_ready():
    print(bmConsole.activated)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(bmMeta.bot_game))

@client.event
async def on_member_join(self, member):
    channel = discord.utils.get(message.guild.channels, name='general')
    logman.log(bmMeta)
    await channel.send(bmGuild.member_joined + "@" + member)


@client.event
async def on_member_remove(self, member):
    channel = discord.utils.get(message.guild.channels, name='general')
    await channel.send(bmGuild.member_left + "@" + member)

@client.event
async def on_commmand_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(bmGuild.command_error)
    print(bmConsole.command_error + f"{error}")

@client.command(brief = 'Reloads cog.', description = 'Do ";reload cog".')
@has_permissions(administrator = True)
async def reload(ctx, extension):
    if ctx.message.author.id in bmMeta.admin_ids:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
    else:
        await ctx.send(bmGuild.insufficient_perms)
        return
    print(bmConsole.cog_reload)
    await ctx.send(bmGuild.cog_reload + extension)

client.load_extension('cogs.fun')
client.load_extension('cogs.admin')
client.load_extension('cogs.useful')
#client.load_extension('cogs.reddit')

client.run(botToken)


