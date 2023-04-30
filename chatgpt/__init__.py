from .Chatgpt import TalkToChatGPTCog
from redbot.core.bot import Red

async def setup(bot: Red):
    cog = TalkToChatGPTCog(bot)
    await bot.add_cog(cog)