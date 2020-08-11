import discord

from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('The Jambot is here. Hello.')

@client.event
async def on_member_join(member):
  print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
  print(f'{member} has left the server. Goodbye!')


@client.command()
async def anime(ctx):
  await ctx.send('No anime!')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def lyne(ctx):
  await ctx.send('http://www.risk-uk.com/wp-content/uploads/2015/04/JamesLyneSANSCyberAcademy1.png')

@client.command()
async def github(ctx):
  await ctx.send('https://github.com/RealJammy/The-Jambot/blob/master/README.md')

@client.command()
async def noleek(ctx):
  await ctx.send('https://game.joincyberdiscovery.com/assets/videos/cheating_message.mp4?version=4.2.0')
                 
@client.command()
@commands.has_permissions(administrator=True)
async def byebye(ctx, amount=5):
  await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason) 


client.run('[put your bot token in here lads]')
