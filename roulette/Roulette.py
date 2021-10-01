# Roulette
import random
import time
from redbot.core import commands
import asyncio

class roulette(commands.Cog):
    """Roulette"""

    def __init__(self, bot):
        self.bot = bot

    #main function
    @commands.command()
    async def roulette(self, ctx):
        """Feeling lucky?"""

        #variables
        player = ctx.author

        #start the game
        await ctx.send("Feelin' lucky?")
        #pause for dramatic effect
        time.sleep(3)
        #perform the 50/50 coin flip
        coin_flip = [0,1]
        random.choice(coin_flip)
        if coin_flip == 0:
            return await ctx.send('Cya idiot')
        else:
            return await ctx.send('Safe for now')






