import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('The Jambot is here. Hello.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Watching over skids'))

@client.event
async def on_member_join(self, member): 
    channel = discord.utils.get(message.guild.channels, name='general')
    await channel.send(f'{member} has joined the server. :smile:')

@client.event
async def on_member_remove(self, member):
    channel = discord.utils.get(message.guild.channels, name='general')
    await channel.send(f'{member} has left the server. :pensive:')

@client.event
async def on_commmand_error(self, ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please give all the arguments.')
    print(f"ERROR: {error}")

@client.command(brief = 'Reloads cog.', description = 'Do ";reload cog".')
@has_permissions(administrator = True)
async def reload(ctx, extension):
    if ctx.message.author.id == 448519423901433876:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
    else:
        await ctx.send("You must be Jammy.")
        return
    
    await ctx.send(f'Successfully reloaded "{extension}".')

client.load_extension('cogs.fun')
client.load_extension('cogs.admin')
client.load_extension('cogs.useful')
client.load_extension('cogs.reddit')
client.load_extension('cogs.fiftyfifty')
client.run('')#api key here :)
