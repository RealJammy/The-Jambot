import discord
from discord.ext import commands, tasks
from Crypto.Util.number import *
from datetime import datetime
from datetime import timedelta
import time


class Useful(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief="Decode a number to bytes.")
    async def lb(self, ctx, arg):
        try:
            await ctx.send(long_to_bytes(int(arg)).decode().replace("@", ""))
        except:
            await ctx.send("Failed <:sex:736200562890113055>")

    @commands.command(brief="Encode bytes to numbers")
    async def bl(self, ctx, arg):
        try:
            await ctx.send(arg.from_bytes(s, arg))
        except:
            await ctx.send("Failed <:sex:736200562890113055>")

    @commands.command(brief="Gives a bot discord invite.")
    async def invite(self, ctx):
        await ctx.send(
            "https://discord.com/api/oauth2/authorize?client_id=742802810843693089&permissions=8&scope=bot"
        )

    @commands.command(brief="Gives a link to The Jambot repo.")
    async def repo(self, ctx):
        await ctx.send("https://github.com/RealJammy/The-Jambot")
        await ctx.send("pls star owo")


    @commands.command(brief="Gives a countdown to the chosen exam.")
    async def exam(self, ctx, arg):
        
        examtimes = {
            "biology": [1636362000],
            "chemistry": [1635930000],
            "physics": [1636102800],
            "music": [1636464600],
            "economics": [1635859800],
            "business": [1636378200],
            "dt": [1636032600],
            "sports": [1635859800],
            "maths": [1635757200, 1636448400],
            "compsci": [1635773400, 1636119000],
            "english": [1635843600, 1636016400],
            "geography": [1635765300, 1636110900],
            "history": [1635946200, 1636456500],
            "spanish": [1635851700, 1636024500],
            "art": [1636967700, 1637054100],
            "rs": [1635938100, 1636370100]
            }
        clean = examtimes.get(arg.lower())
        if clean == "None":
            await ctx.send("Subject not found!")
            print(f"The user tried use {arg.lower()}. This obviously doesnt work as it isn't a real subject, right?")
        else:
            message = ""
            clean2 = list(map(time_difference, clean))
            for i,j in enumerate(clean2):
                if j:
                    message += f"The {make_ordinal(i+1)} exam for {arg} will be on {j[0].strftime('%d/%m/%Y at %H:%M')}.\nThat's in {j[1]} days, {j[2]} hours and {j[3]} minutes.\n"
            if not message:
                message += "There are no exams left for this subject.\n"
            await ctx.send(message[:-1])
           
    @commands.command(brief="Displays this message!")
    async def help(self, ctx):
        cogs = self.client.cogs
        helpMessage = discord.Embed(
            title="Help", colour=discord.Colour.purple())
        for cog in cogs:
            commands = self.client.get_cog(cog).get_commands()
            text = "\n".join(
                [f"`{c.name}`: {c.brief} {c.description}" for c in commands]
            )
            helpMessage.add_field(name=f"{cog}", value=text, inline=False)

        await ctx.send(embed=helpMessage)

def make_ordinal(n):
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

def time_difference(then):
    then = datetime.fromtimestamp(then)
    now = datetime.utcnow()
    diff = (then - now).total_seconds()
    if diff <= 0:
        return None
    else:
        minutes = int(diff+59) // 60
        hours  = minutes // 60
        days = hours // 24
        offset = timedelta(hours = 1 if time.localtime().tm_isdst else 0)
        return [then+offset, days, hours%24, minutes%60]
    
def setup(client):
    client.add_cog(Useful(client))
