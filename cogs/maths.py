import discord
from discord.ext import commands
import os
from random import choice as random
from io import BytesIO
from urllib.parse import quote
from aiohttp import ClientSession
from sympy import latex
from sympy.parsing.sympy_parser import parse_expr
import json

LATEX_URL = (
    "https://latex.codecogs.com/png.download?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Chuge%20"
)

with open("resources/file.json") as file:
    data = json.load(file)

class Maths(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        brief="Generate Junior Mathematical Competition problem, usage: .jmc <year>"
    )
    async def jmc(self, ctx, year: int):  # from years 2004 - 2018
        year = str(year)

        try:
            question = data["JMC"][year]["questions"]
        except:
            await ctx.send("Sorry, can only be between 2004-2018")
            return

        question = random(question)

        embed = discord.Embed(title="JMC-"+year, colour=0x00008B)
        embed.set_image(url=question)
    
        await ctx.send(embed=embed)

    @commands.command(
        brief="Generate Intermediate Mathematical Competition problem, usage: .imc <year>"
    )
    async def imc(self, ctx, year: int):  # from years 2004 - 2018
        year = str(year)

        try:
            question = data["IMC"][year]["questions"]
        except:
            await ctx.send("Sorry, can only be between 2004-2018")
            return

        question = random(question)

        embed = discord.Embed(title="IMC-"+year, colour=0x00008B)
        embed.set_image(url=question)
    
        await ctx.send(embed=embed)
        

    @commands.command(
        brief="Generate Senior Mathematical Competition problem, usage: .smc <year>"
    )
    async def smc(self, ctx, year: int):  # from years 2005 - 2018
        year = str(year)

        try:
            question = data["SMC"][year]["questions"]
        except:
            await ctx.send("Sorry, can only be between 2005-2018")
            return

        question = random(question)

        embed = discord.Embed(title="SMC-"+year, colour=0x00008B)
        embed.set_image(url=question)
    
        await ctx.send(embed=embed)

    @commands.command(brief="Latex")
    async def latexify(self, ctx, expr: str):
        fixed_expr = expr.replace("^", "**")
        try:
            parsed = parse_expr(fixed_expr, evaluate=False)
        except SyntaxError:
            await ctx.send("Invalid expression!")
        else:
            ltx = latex(parsed)
            urlsafe = quote(ltx)
            async with ClientSession() as session:
                async with session.get(LATEX_URL + urlsafe) as resp:
                    bytes_img = await resp.read()

            file = discord.File(fp=BytesIO(bytes_img), filename="latex.png")
            await ctx.send(file=file)

def setup(client):
    client.add_cog(Maths(client))
