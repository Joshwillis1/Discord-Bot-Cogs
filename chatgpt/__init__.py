from .chatgpt import Chatgpt
from redbot.core.bot import Red

async def setup(bot: Red):
    cog = Assistant(bot)
    await bot.add_cog(cog)