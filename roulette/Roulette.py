# Roulette
import random
import time
from typing import Counter
import discord
from redbot.core import checks, commands
from discord.ext.commands import bot_has_permissions, Bot, BotMissingPermissions

class roulette(commands.Cog):
    """Roulette"""

    def __init__(self, bot):
        self.bot = bot

    #coin flip
    @commands.command()
    @bot_has_permissions(kick_members = True)
    async def roulette(self, ctx):
        """Feeling lucky?"""

        author = ctx.message.author

        #start the game
        await ctx.send("Feelin' lucky?")
        #pause for dramatic effect
        time.sleep(3)
        #perform the 50/50 coin flip
        coin_flip = random.choice([0,1])
        if coin_flip == 0:
            #check to see if user is admin
            if ctx.author.server_permissions.administrator:
                return await ctx.send('User is administrator and is cannot be kicked.. Loser')
            else:
                #losing roll = kick from server
                await ctx.send('Cya idiot')
                #send message to user before kick with a server invite
                await ctx.author.send(await ctx.channel.create_invite(max_uses=1,unique=True))
                #perform the kick
                await author.kick()
        elif coin_flip == 1:
            #winning roll = not kick
            return await ctx.send('Safe for now')