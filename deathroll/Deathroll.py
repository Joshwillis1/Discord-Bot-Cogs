# Deathroll
from random import randrange
from redbot.core import commands
import asyncio

class deathroll(commands.Cog):
    """Deathroll"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def deathroll(self, ctx, amount):
        """Let's play deathroll"""
        if [game for game in self.games if game.ctx.channel == ctx.channel]:
            return await ctx.send('A game is already running in this channel.')

        if int(amount) > 9999999:
            return await ctx.send("fuck off idiot")

        playerOne = ctx.author.display_name
        playerTwo = ""
        bet = amount
        roll = 0
        turn = ""
        check = lambda m: (
            not m.author.bot
            and m.channel == ctx.message.channel
            and (
                (m.author != ctx.message.author and m.content.lower() == 'i')
                or (m.author == ctx.message.author and m.content.lower() == 'ai')
            )
        )

        game = deathroll(self, ctx)
        self.games.append(game)

        await ctx.send('Second player, say I.')
        try:
            r = await self.bot.wait_for('message', timeout=60, check=check)
            playerTwo = r.author.display_name
        except asyncio.TimeoutError:
            return await ctx.send('Nobody else wants to play, shutting down.')

        # This randomly selects who goes first.
        randp = randrange(1, 3, 1)
        if randp == 1:
            turn = playerOne
        else:
            turn = playerTwo
        # Sets the initial roll
        roll = int(bet)
        while roll > 1:
            # Prints who's turn it is and waits for any key.
            await ctx.send(turn + "'s turn | " + "1 - " + ('{:,}'.format(roll))) # ('{:,}'.format(roll))
            # Rolls the number and prints.
            rand = randrange(1, (roll + 1), 1)
            await ctx.send(turn + " rolls a " + str(('{:,}'.format(rand))))
            roll = rand
            # Checks to see if player lost
            if roll == 1:
                continue
            # Changes to the next player.
            if turn == playerOne:
                turn = playerTwo
            else:
                turn = playerOne
        # Display winner and losser 
        winner = ""
        losser = turn

        if losser == playerOne:
            winner = playerTwo
        else:
            winner = playerOne

        await ctx.send("------------------------------")
        await ctx.send(losser + " losses and must pay " + winner + " " + ('{:,}'.format(int(bet))) + "!")           
    
