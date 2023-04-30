from .Chatgpt import TalkToChatGPTCog
from redbot.core.bot import Red

def setup(bot: Red):
    cog = TalkToChatGPTCog(bot)
    bot.add_cog(cog)   
    
    #cog = TalkToChatGPTCog(bot)
    #bot.add_cog(TalkToChatGPTCog(bot))