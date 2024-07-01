# card game
import random

random.seed(random.randint(1,1000))

deck = []
colours = ["Red", "Yellow", "Black"]
player1_cards = []
player2_cards = []


class Card:
    def __init__(self, colour:str, number:int):
        self.colour = colour
        self.number = number

    def get_colour(self):
        return self.colour

    def get_number(self):
        return self.number


for x in range(1,11):
    print("Iteration: " + str(x))
    y = Card("Red", x)
    z = Card("Yellow", x)
    a = Card("Black", x)

    deck.append(y)
    deck.append(z)
    deck.append(a)
    
for y in deck:
    print("Card:" + y.get_colour() + " " + str(y.get_number()))


# main game
while len(deck) > 0:
    #game continues
    card1 = random.choice(deck)
    deck.remove(card1)
    card2 = random.choice(deck)
    deck.remove(card2)

    cards = [card1, card2]
    cards_colours = [card1.get_colour(), card2.get_colour()]
    
    print("Player 1 has the card: " + card1.get_colour() + " " + str(card1.get_number()))
    print("Player 2 has the card: " + card2.get_colour() + " " + str(card2.get_number()))
    
    #compare cards
    if card1.get_colour() == card2.get_colour():
        #they are the same colour
        print("Both cards are the same colour, the numbers shall be compared!")
        if card1.get_number() > card2.get_number():
            #player1 has won and gets both cards
            print("Player 1's card has a greater number and has won!")
            player1_cards.append(card1)
            player1_cards.append(card2)
        elif card1.get_number() < card2.get_number():
            #player2 has won
            print("Player 2's card has a greater number and has won!")  
            player2_cards.append(card1)
            player2_cards.append(card2)
        else:
            #this isn't even possible
            print("How did we get here?")

            
    else:
        #they are not the same colour
        print("The cards are not the same colour!")
        if card_colours[0] == "Red" and card_colours[1] == "Black":
            #card1 (player1) will win
    





