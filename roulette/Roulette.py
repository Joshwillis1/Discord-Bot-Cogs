# Roulette
import random
from redbot.core import commands
import asyncio

class roulette(commands.Cog):
    """Roulette"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roulette(self, ctx):
        """Feeling lucky?"""

        check = lambda m: (
            not m.author.bot
            and m.channel == ctx.message.channel
            and (
                (m.author != ctx.message.author and m.content.lower() == 'i')
                or (m.author == ctx.message.author and m.content.lower() == 'ai')
            )
        )

        chambers = await ctx.send('Enter number of bullets (2-6)')

        try:
            r = await self.bot.wait_for('message', timeout=60, check=check)
            if int(r) > 6:
                await ctx.sent(r + 'greater')
                return await ctx.send('Bullets must be less than or equal to 6')
            elif int(r) < 2:
                await ctx.sent(r + 'lower')
                return await ctx.send('Bullets must be greater than or equal to 2')
            elif not r.isdigit():
                await ctx.sent(r + 'not digit')
                return await ctx.send('Bullets must be a number betweeen 2 and 6')
            else:
                chambers = int(r)
        except asyncio.TimeoutError:
            return await ctx.send('Timed out, try again')



