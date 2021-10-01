# Roulette
import random
import time
from typing import Counter
import discord
from redbot.core import checks, commands
import asyncio

class roulette(commands.Cog):
    """Roulette"""

    def __init__(self, bot):
        self.bot = bot

    #main function
    @commands.command()
    @checks.admin_or_permissions(kick_members=True)
    @checks.bot_has_permissions(kick_members=True)
    async def roulette(self, ctx):
        """Feeling lucky?"""

        #variables
        player = ctx.author

        #start the game
        await ctx.send("Feelin' lucky?")
        #pause for dramatic effect
        time.sleep(3)
        #perform the 50/50 coin flip
        coin_flip = random.choice(0,1)
        if coin_flip == 0:
            return  await ctx.send('Cya idiot')
        elif coin_flip == 1:
            return await ctx.send('Safe for now')






