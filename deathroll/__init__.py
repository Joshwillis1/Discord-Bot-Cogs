from .deathroll import deathroll


def setup(bot):
    bot.add_cog(deathroll(bot))