# Roulette
import random
import time
from typing import Counter
import discord
from redbot.core import checks, commands
import asyncio
from discord.ext.commands import has_permissions, CheckFailure, BadArgument

class roulette(commands.Cog):
    """Roulette"""

    def __init__(self, bot):
        self.bot = bot

    #main function
    @commands.command()
    async def roulette(self, ctx):
        """Feeling lucky?"""

        result = ""

        #start the game
        await ctx.send("Feelin' lucky?")
        #pause for dramatic effect
        time.sleep(3)
        #perform the 50/50 coin flip
        coin_flip = random.choice([0,1])
        if coin_flip == 0:
            await ctx.send('Cya idiot')
            return result
        elif coin_flip == 1:
            await ctx.send('Safe for now')
            return result
        
        await ctx.send (result)









