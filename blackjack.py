"""BlackJack, project idea from Al Sweigart """
import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = "backside"

def main():

    print("""RULES:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.""")

money = 5000
while True:

    if money <= 0:
        print("You're out of funds")
        print("Good thing, this wasn't real money.")
        print("Thanks for playing!")
        sys.exit()

    print(f"MONEY: ${money}")
    bet = getBet(money)
    
    return 0

def getBet(maxBet):
    print("How much ")



if __name__ == "__main__":
    main()
