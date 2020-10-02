import discord
from discord.ext import commands
import os
import random
from io import BytesIO
from urllib.parse import quote
from aiohttp import ClientSession
from sympy import latex
from sympy.parsing.sympy_parser import parse_expr

LATEX_URL = "https://latex.codecogs.com/png.download?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Chuge%20"

class Maths(commands.Cog):

  def __init__(self,client):
    self.client = client

  @commands.command(brief = "Generate Junior Mathematical Competition problem, usage: .jmc <year>")
  async def jmc(self, ctx, year): # from years 2004 - 2018
    try:
      allProblems = os.listdir("MATHS-IMAGES/junior/" + year)
      problem = random.choice(allProblems)
      await ctx.send(file=discord.File("MATHS-IMAGES/junior/" + year + "/" + problem))
    except:
      await ctx.send("Junior Mathematical Competition problems only available from 2004 to 2018")

  @commands.command(brief = "Generate Intermediate Mathematical Competition problem, usage: .imc <year>")
  async def imc(self, ctx, year): # from years 2004 - 2018
    try:
      allProblems = os.listdir("MATHS-IMAGES/intermediate/" + year)
      problem = random.choice(allProblems)
      await ctx.send(file=discord.File("MATHS-IMAGES/junior/" + year + "/" + problem))
    except:
      await ctx.send("Intermediate Mathematical Competition problems only available from 2004 to 2018")
  
  @commands.command(brief = "Generate Senior Mathematical Competition problem, usage: .smc <year>")
  async def smc(self, ctx, year): # from years 2005 - 2018
    try:
      allProblems = os.listdir("MATHS-IMAGES/senior/" + year)
      problem = random.choice(allProblems)
      await ctx.send(file=discord.File("MATHS-IMAGES/senior/" + year + "/" + problem))
    except:
      await ctx.send("Senior Mathematical Competition problems only available from 2005 to 2018")

  @commands.command(brief = "Latex")
  async def latexify(self, ctx, expr: str):
      fixed_expr = expr.replace('^', '**')
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