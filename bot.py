import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import json

client = commands.Bot(command_prefix=".", status=discord.Status.online, activity=discord.Game("with the on and off switch"))
client.remove_command("help")

with open("creds.json", "r") as creds:
    data = json.load(creds)["creds"]
    token = data["bot_token"]


@client.event
async def on_ready():
    print("The Jambot is here. Hello.")


@client.event
async def on_member_join(self, member):
    channel = discord.utils.get(message.guild.channels, name="general")
    await channel.send(f"{member} has joined the server. :smile:")


@client.event
async def on_member_remove(self, member):
    channel = discord.utils.get(message.guild.channels, name="general")
    await channel.send(f"{member} has left the server. :pensive:")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("Please give all the arguments.")
    elif isinstance(error, commands.errors.BadArgument):
        await ctx.send("Conversion of arguments failed.")
    print(f"ERROR: {error}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content == "Who are the cyberists?":
            await ctx.send("The Cyberists are the ones who created the Jambot.")


client.load_extension("cogs.fun")
client.load_extension("cogs.admin")
client.load_extension("cogs.useful")
client.load_extension("cogs.reddit")
client.load_extension("cogs.maths")
client.run(token)  # api key here :)
