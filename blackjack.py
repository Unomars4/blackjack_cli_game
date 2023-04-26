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

        print(f"Bet: ${bet}")
        while True:
            
            displayHands(playerhand, dealerhand, False)
            if getHandValue(playerhand) > 21:
                break

            move = getMove(playerhand, money)

    
    
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

def getMove(cards, money):
    return

def displayHands(playerhand, dealerhand, showdealerhand):
    
    if showdealerhand:
        print(f"Dealer: ${getHandValue(dealerhand)}")
        displayCards(dealerhand)
    else:
        print("Dealer: ???")
        displayCards([BACKSIDE] + dealerhand[1:])

    print(f"Player: ${getHandValue(playerhand)}")
    displayCards(playerhand)


def getHandValue(cards):
    value = 0
    nofAces = 0
    
    for card in cards:
        rank = card[0]
        if rank == "A":
            nofAces += 1
        elif rank in ["K", "Q", "J"]:
            value += 10
        else:
            value += int(rank)

    value += nofAces
    for i in range(nofAces):
        if value + 10 > 21:
            break
        else:
            value += 10

    return value

def displayCards(cards):
    return

if __name__ == "__main__":
    main()
