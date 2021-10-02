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
    @has_permissions(kick_members=True)
    @checks.bot_has_permissions(kick_members=True)
    async def roulette(self, ctx):
        """Feeling lucky?"""

        #start the game
        await ctx.send("Feelin' lucky?")
        #pause for dramatic effect
        time.sleep(3)
        #perform the 50/50 coin flip
        coin_flip = random.choice([0,1])
        if coin_flip == 0:
            await ctx.send('Cya idiot')
            if ctx.author.server_permissions.administrator:
                return await ctx.send ('User is admin and cannot face consequences')
            else:
                try:
                    await ctx.kick(ctx.author)
                except Exception:
                    await ctx.send('Something went wrong')
        elif coin_flip == 1:
            return await ctx.send('Safe for now')






