import discord                                                                                                                                                                                                                             
import random                                                                                                                                                                                                                              
from discord.ext import commands                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
client = commands.Bot(command_prefix = '.')                                                                                                                                                                                                
                                                                                                                                                                                                                                           
@client.event                                                                                                                                                                                                                              
async def on_ready():                                                                                                                                                                                                                      
  print('The Jambot is here. Hello.')                                                                                                                                                                                                      
  await client.change_presence(status=discord.Status.online, activity=discord.Game('Watching over skids'))                                                                                                                                 
@client.event                                                                                                                                                                                                                              
async def on_member_join(member):                                                                                                                                                                                                          
  print(f'{member} has joined the server.')                                                                                                                                                                                                
                                                                                                                                                                                                                                           
@client.event                                                                                                                                                                                                                              
async def on_member_remove(member):                                                                                                                                                                                                        
  print(f'{member} has left the server.Goodbye!')                                                                                                                                                                                          
                                                                                                                                                                                                                                           
@client.event                                                                                                                                                                                                                              
async def on_command_error(ctx, error):                                                                                                                                                                                                    
  if isinstance(error, commands.MissingRequiredArgument):                                                                                                                                                                                  
    await ctx.send('Please give all the arguments.')                                                                                                                                                                                       
                                                                                                                                                                                                                                           
@client.command()                                                                                                                                                                                                                          
async def anime(ctx):                                                                                                                                                                                                                      
  image = discord.Embed()                                                                                                                                                                                                                  
  image.set_image(url=f'https://www.thiswaifudoesnotexist.net/example-{__import__("random").randint(0, 100000)}.jpg')                                                                                                                      
  await ctx.send(embed=image)                                                                                                                                                                                                              
                                                                                                                                                                                                                                           
@client.command()                                                                                                                                                                                                                          
async def noanime(ctx):                                                                                                                                                                                                                    
  await ctx.send('https://i.kym-cdn.com/entries/icons/original/000/027/108/anime.jpg')                                                                                                                                                     
                                                                                                                                                                                                                                           
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

@client.command()
@commands.has_permissions(administrator=True)
async def gotosleep(ctx, role_id: 736248018139086911):
  awake = [member.id for member in ctx.guild.get_role(role_id).members if member.status != Status.offline]
  text = f'{["<@"+id+">" for id in awake].join()} GO TO SLEEP'
  await ctx.send(text)
  
 
client.run('[put your bot token in ere innit]')
