# Deathroll
from random import randrange
from redbot.core import commands

class deathroll(commands.Cog):
    """Deathroll"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def deathroll(self, ctx, player1, player2, amount):
        """Let's play deathroll"""
        playerOne = player1
        playerTwo = player2
        bet = amount
        roll = 0
        turn = ""
        await ctx.send("Player one = " + playerOne + " Player two = " + playerTwo + " Bet ammount = " + ('{:,}'.format(int(bet))))

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
    
