from .Roulette import roulette


def setup(bot):
    bot.add_cog(roulette(bot))