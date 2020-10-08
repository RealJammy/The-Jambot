import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        brief="Clear messages in channel (default 5).",
        description='Do ".byebye amount_to_clear".',
    )
    @commands.has_permissions(administrator=True)
    async def byebye(
        self, ctx, amount=6
    ):  # 6 because it needs to clear the command message too
        await ctx.channel.purge(limit=amount + 1)

    @commands.command(
        brief="Kicks users.", description='Do ".kick @user".'
    )  # Just testing on kick first will do ban after
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, user: discord.Member, reason=None):
        try:
            await user.kick(reason=reason)
            await commands.send_message(
                user,
                "Damn, I'm just a lowly bot but even I think you should have been kicked :pensive:",
            )
        except discord.Forbidden:
            await ctx.send("Could not kick user. Check my permissions.")

    @commands.command(brief="Bans users.", description='Do ".ban @user".')
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user: discord.Member, reason=None):
        try:
            await user.ban(reason=reason)
            await commands.send_message(
                user,
                "Damn, I'm just a lowly bot but even I think you should have been banned :pensive:",
            )
        except discord.Forbidden:
            await ctx.send("Could not ban user. Check my permissions.")

    @commands.command(brief="Unbans users.", description='Do ".unban [id]"')
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, id: int, reason=None):
    	try:
    		user = await self.client.fetch_user(id)
    		await ctx.message.guild.unban(user, reason=reason)
    		await ctx.send(f'{user.name}#{user.discriminator} has been unbanned!')
    	except discord.Forbidden:
    		await ctx.send("Could not unban user. Check my permissions.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def gotosleep(self, ctx, role_id: int = 736248018139086911):
        awake = [
            member
            for member in ctx.guild.get_role(role_id).members
            if member.status != discord.Status.offline and not member.bot
        ]
        text = "".join(f"<@{member.id}> " for member in awake) + "GO TO SLEEP"
        await ctx.send(text)


# TODO: add automated version at some point e.g. every night at ~3am it gets online users and tells em to sleep.


def setup(client):
    client.add_cog(Admin(client))
