import random

suits = {'spades': '♠','diamonds': '♦', 'clubs': '♣', 'hearts': '♥'}#dictionary to change suits to symbols
cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] #list of cards 
deck = list()#the deck

for suit in suits:
    for card in cards: #for each card in the cards list
        deck.append(f"{card} of {suits[suit]}") #add a suit from suits to each card

#shuffle
shuffle = random.shuffle(deck)

print("You got:")
for i in range(5):#the amount of cards drawn
   print(deck[i])#drawing the crads/printing them
   