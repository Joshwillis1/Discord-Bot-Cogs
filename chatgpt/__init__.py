from .chatgpt import ChatGPT
from redbot.core.bot import Red


def setup(bot: Red):  
    bot.add_cog(ChatGPT(bot))