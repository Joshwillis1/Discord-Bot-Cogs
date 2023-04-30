from .Chatgpt import chatgpt


def setup(bot):
    bot.add_cog(chatgpt(bot))