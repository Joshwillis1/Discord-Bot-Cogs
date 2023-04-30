from .chatgpt import ChatGPT


def setup(bot: Red):  
    bot.add_cog(ChatGPT(bot))