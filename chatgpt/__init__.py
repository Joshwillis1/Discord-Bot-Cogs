from .Chatgpt import Chatgpt
from redbot.core.bot import Red

async def setup(bot: Red):
    cog = chatgpt(bot)
    await bot.add_cog(cog)