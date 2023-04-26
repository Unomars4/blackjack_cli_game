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

        print(f"Money: ${money}")
        bet = getBet(money)
        if not bet:
            break

        deck = getDeck()
        dealerhand = [deck.pop(),deck.pop()]
        playerhand = [deck.pop(),deck.pop()]
    
    
    print("Thanks for playing")


def getBet(maxBet):
    
    bet = 0
    while True:
        print(f"How much do you want to bet this round? (${maxBet} or QUIT)")
        response = input("> ").upper()
        if response == "QUIT":
            break
        if not response.isdecimal():
            continue
        if 0 < int(response) <= maxBet:
            bet = int(response)
            break
    return bet

def getDeck():
    
    deck = []
    for suit in [DIAMONDS, HEARTS, SPADES, CLUBS]:
        for rank in range(2,11):
            deck.append((rank, suit))
        for rank in ["J", "K", "Q", "A"]:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


if __name__ == "__main__":
    main()
