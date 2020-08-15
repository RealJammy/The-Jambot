import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
#import schedule, time #to be used for the last function in here (probably, i think)

class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    #EVENTS

    @commands.Cog.listener() #check if this works instead of going off of ur old code jamie
    async def on_ready(self):
        print('The Jambot is here. Hello.')
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Watching over skids'))

    @commands.Cog.listener()
    async def on_member_join(self, member): #also check if this works lol- will run one big test at the end probably
        channel = discord.utils.get(message.guild.channels, name='general')
        await channel.send(f'{member} has joined the server. :smile:')

    @commands.Cog.listener()
    async def on_member_remove(self, member): #should probably stop putting a note to check at every function lmao
        channel = discord.utils.get(message.guild.channels, name='general')
        await channel.send(f'{member} has left the server. :pensive:')
    
    @commands.Cog.listener()
    async def on_commmand_error(self, ctx, error): 
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please give all the arguments.')
        print(f"ERROR: {error}")

    #ACTUAL ADMIN STUFF (im not screaming, my eyesight is just poor so it helps me see)

    @commands.command(brief='Clear messages in channel (default 5).', description='Do ".byebye amount_to_clear".')
    @commands.has_permissions(administrator=True)
    async def byebye(self, ctx, amount=6): #6 because it needs to clear the command message too
   	    await ctx.channel.purge(limit=amount+1)

    @commands.command(brief='Kicks users.', description='Do ".kick @user".') #Just testing on kick first will do ban after
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, userName, discord.User):
        await member.kick(userName)#Why is it member.kick and not bot.kick?
        #await bot.kick(userName)#One of these 2 should work, just test each one. Commented out bottom line for testing.
        #await commands.send_message(user, "Damn, I'm just a lowly bot but even I think you should have been kicked :pensive:")

    @commands.command(brief='Bans users.', description='Do ".ban @user".')
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        user = await commands.get_user_info(member.ID)
        await member.ban(reason=reason)
        await commands.send_message(user, "Damn, I'm just a lowly bot but even I think you should have been banned :pensive:")

   # USING AUTOMATED VERSION INSTEAD- JAMMY JUST SAY IF YOU WANT THIS TOO
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def gotosleep(self, ctx, role_id: int = 736248018139086911):
        awake = [member for member in ctx.guild.get_role(role_id).members if member.status != discord.Status.offline and not member.bot]
        text = ''.join(f'<@{member.id}> ' for member in awake) + "GO TO SLEEP"
        await ctx.send(text)

   # add automated version at some point- like every night at 3am it gets online users and tells em to sleep.

def setup(client):
    client.add_cog(admin(client))
