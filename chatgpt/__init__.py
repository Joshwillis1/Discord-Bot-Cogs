from .chatgpt import TalkToChatGPTCog
from redbot.core.bot import Red

def setup(bot: Red):  
    #cog = TalkToChatGPTCog(bot)
    bot.add_cog(TalkToChatGPTCog(bot))