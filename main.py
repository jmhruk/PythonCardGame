# card game
import random
import time

random.seed(random.randint(1,1000))

deck = []
colours = ["Red", "Yellow", "Black"]
player1_cards = []
player2_cards = []
p1won = False
p2won = False
authenticated = False
class Card:
    def __init__(self, colour:str, number:int):
        self.colour = colour
        self.number = number

    def get_colour(self):
        return self.colour

    def get_number(self):
        return self.number

def displayCards(cards):
    s = ""
    for x in cards:
        s = s + x.get_colour() + " " + str(x.get_number()) + ", "
    return s

for x in range(1,11):
    #print("Iteration: " + str(x))
    y = Card("Red", x)
    z = Card("Yellow", x)
    a = Card("Black", x)

    deck.append(y)
    deck.append(z)
    deck.append(a)

# testing method to make sure cards are being created correctly  
#for y in deck:
    #print("Card:" + y.get_colour() + " " + str(y.get_number()))

while authenticated == False:
    authenticated = True
else:
    #Game starts
    
    # main game
    while len(deck) > 0:
        time.sleep(1)
        print()
        print("New Round:")
        #game continues
        card1 = random.choice(deck)
        deck.remove(card1)
        card2 = random.choice(deck)
        deck.remove(card2)

        cards = [card1, card2]
        card_colours = [card1.get_colour(), card2.get_colour()]
        
        print("Player 1 has the card: " + card1.get_colour() + " " + str(card1.get_number()))
        print("Player 2 has the card: " + card2.get_colour() + " " + str(card2.get_number()))
        print()
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
                print("Player 1's card is Red and has beat Player 2's Black Card!")
                player1_cards.append(card1)
                player1_cards.append(card2)
            if card_colours[0] == "Black" and card_colours[1] == "Red":
                print("Player 2's card is Red and has beat Player 1's Black Card!")
                player2_cards.append(card1)
                player2_cards.append(card2)
            if card_colours[0] == "Yellow" and card_colours[1] == "Red":
                print("Player 1's card is Yellow and has beat Player 2's Red Card!")
                player1_cards.append(card1)
                player1_cards.append(card2)
            if card_colours[0] == "Red" and card_colours[1] == "Yellow":
                print("Player 2's card is Yellow and has beat Player 1's Red Card!")
                player2_cards.append(card1)
                player2_cards.append(card2)
            if card_colours[0] == "Black" and card_colours[1] == "Yellow":
                print("Player 1's Card is Black and has beat Player 2's Yellow Card!")
                player1_cards.append(card1)
                player1_cards.append(card2)
            if card_colours[0] == "Yello" and card_colours[1] == "Black":
                print("Player 2's Card is Black and has beat Player 1's Yellow Card!")
                player2_cards.append(card1)
                player2_cards.append(card2)

            time.sleep(1)
            print()
            print("Player 1's Cards: " + displayCards(player1_cards))
            print()
            print("Player 2's Cards: " + displayCards(player2_cards))
        
                    
    else:
        time.sleep(1)
        # game ending system
        player1_score = len(player1_cards)
        player2_score = len(player2_cards)

        if player1_score == player2_score:
            # overtime
            p1n = random.randint(1,10)
            p2n = random.randint(1,10)

            while p1n == p2n:
                p1n = random.randint(1,10)
                p2n = random.randint(1,10)
            else:
                if p1n > p2n:
                    print("Player 1 has won!")
                    p1won = True
                else:
                    print("Player 2 has won!")
                    p2won = True
        print()
        if player1_score > player2_score:
            print("Player 1 has won!")
            p1won = True
            print("Their Cards were: " + displayCards(player1_cards))
        else:
            print("Player 2 has won!")
            p2won = True
            print("Their Cards were: " + displayCards(player2_cards))

        # file reading and saving

            



            

            
                






