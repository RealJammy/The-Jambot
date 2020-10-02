import discord
from discord.ext import commands
import os
import random

class UKMT(commands.Cog):

  def __init__(self,client):
    self.client = client

  @commands.command(brief = "Generate JMC problem, usage: .jmc <year>")
  async def jmc(self, ctx, year): # from years 2004 - 2018
    try:
      allProblems = os.listdir("MATHS-IMAGES/junior/" + year)
      problem = random.choice(allProblems)
      await ctx.send(file=discord.File("MATHS-IMAGES/junior/" + year + "/" + problem))
    except:
      await ctx.send("Junior Mathematical Competition problems only available from 2004 to 2018")

  @commands.command(brief = "Generate IMC problem, usage: .imc <year>")
  async def imc(self, ctx, year): # from years 2004 - 2018
    try:
      allProblems = os.listdir("MATHS-IMAGES/intermediate/" + year)
      problem = random.choice(allProblems)
      await ctx.send(file=discord.File("MATHS-IMAGES/junior/" + year + "/" + problem))
    except:
      await ctx.send("Intermediate Mathematical Competition problems only available from 2004 to 2018")

  @commands.command(brief = "Generate SMC problem, usage: .smc <year>")
  async def smc(self, ctx, year): # from years 2005 - 2018
    try:
      allProblems = os.listdir("MATHS-IMAGES/senior/" + year)
      problem = random.choice(allProblems)
      await ctx.send(file=discord.File("MATHS-IMAGES/senior/" + year + "/" + problem))
    except:
      await ctx.send("Senior Mathematical Competition problems only available from 2005 to 2018")

def setup(client):
  client.add_cog(UKMT(client))
