# Deathroll
from random import randrange
from redbot.core import commands

class deathroll(commands.Cog):
    """Deathroll"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def deathroll(self, ctx, *, entered_title):
        """Let's play deathroll"""
        await ctx.send("I can do stuff!"+entered_title)
        return
        playerOne = ""
        playerTwo = ""
        bet = ""
        ready = ""
        roll = 0
        turn = ""

        def getPlayers():
            global playerOne, playerTwo
            print("Player one enter your name here:")
            playerOne = input()
            print("Player one = " + playerOne)
            print("Player two enter your name here:")
            playerTwo = input()
            print("Player two = " + playerTwo)

        def getBet():
            global bet
            print("Bet ammount:")
            bet = input()
            print("bet ammount = " + ('{:,}'.format(int(bet))))

        getPlayers()
        getBet()

        while True:
            print("Player one = " + playerOne + " Player two = " + playerTwo + " Bet ammount = " + ('{:,}'.format(int(bet))))
            print("Are you ready? y/n")
            ready = input()

            if ready == "y":
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
                    print(turn + "'s turn, press enter to continue | " + "1 - " + ('{:,}'.format(roll))) # ('{:,}'.format(roll))
                    input()
                    # Rolls the number and prints.
                    rand = randrange(1, (roll + 1), 1)
                    print(turn + " roll's a " + str(('{:,}'.format(rand))))
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

                print("------------------------------")
                print(losser + " losses and must pay " + winner + " " + ('{:,}'.format(int(bet))) + "!")

            print("Would you like to play again?")
            again = input()
            if again == "y":
                print("Would you like to use the same names?")
                again = input()
                if again == "y":
                    getBet()
                else:
                    getPlayers()
                    getBet()
            else:
                break
        
