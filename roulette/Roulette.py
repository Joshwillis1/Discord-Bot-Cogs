# Roulette
import random
from redbot.core import commands

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
                return await ctx.send('Bullets must be less than or equal to 6')
            elif int(r) < 2:
                return await ctx.send('Bullets must be greater than or equal to 2')
            elif not r.isdigit():
                return await ctx.send('Bullets must be a number betweeen 2 and 6')
            else:
                chambers = int(r)
        except:
            return await ctx.send('you broke it, dork')



