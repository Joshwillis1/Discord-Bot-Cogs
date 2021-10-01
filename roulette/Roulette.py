# Roulette
import random
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
        chambers = ""

        #this is needed to check user response
        check = lambda m: (
            not m.author.bot
            and m.channel == ctx.message.channel
            and (
                (m.author != ctx.message.author and m.content.lower() == 'i')
                or (m.author == ctx.message.author and m.content.lower() == 'ai')
            )
        )

        #ask user how many bullets (chances) they would like and wait for response
        await ctx.send('Enter number of bullets (2-6)')
        try:
            r = await self.bot.wait_for('message', timeout=60, check=check)
            chambers = r.int()
        except asyncio.TimeoutError:
            return await ctx.send('Timed out, try again')



