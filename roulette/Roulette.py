# Roulette
import random
import time
from typing import Counter
import discord
from redbot.core import checks, commands
import asyncio
from discord.ext import commands

class roulette(commands.Cog):
    """Roulette"""

    def __init__(self, bot):
        self.bot = bot



    #coin flip
    @commands.command()
    @commands.has_permissions(kick_members=True)
    @bot.command(pass_context = True)
    async def roulette(self, ctx):
        """Feeling lucky?"""

        bot = commands.Bot()
        author = ctx.message.author

        #start the game
        await ctx.send("Feelin' lucky?")
        #pause for dramatic effect
        time.sleep(3)
        #perform the 50/50 coin flip
        coin_flip = random.choice([0,1])
        if coin_flip == 0:
            await ctx.send('Cya idiot')
            await bot.kick(author)
        elif coin_flip == 1:
            return await ctx.send('Safe for now')