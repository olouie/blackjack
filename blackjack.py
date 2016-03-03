import random
#import os
#os.system('clear')

class Deck(object):
    
    # A deck needs 52 cards, consisting of 13 ranks of 4 different suits
     
    suits = ('hearts', 'spades', 'diamonds', 'clubs')
    ranks = {'ace':11, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 
             'ten':10, 'jack':10, 'queen':10, 'king':10}  
    
    stack = {}
    
    for suit in suits:
        for k,v in ranks.iteritems():
            stack[k + ' of ' + suit] = v
    
    def __init__(self):
        print 'Deck has been created'

    def deck_total(self): 
    # Displays total cards remaining
        print "There are %d cards left in this deck" %len(Deck.stack)

    def random_card(self): 
    # Chooses one card at random
        card = random.choice(Deck.stack.keys())
        return card

    def del_card(self):
        # Deletes card chosen at random
        x = self.random_card()
        Deck.stack.pop(x)
        return x

class Player(Deck):

    # A player should be dealt 2 cards at random, have the ability to discard 1-2 cards, draw 1-2 cards at random
    # Create class variable to hold the hand of the player
    # Splitting a hand will not be in this time

    hand = []

    def __init__(self):
        self.deck = Deck()

    def show_hand(self):
        print Player.hand

    def draw(self):
        # Adds a randomly chosen card to Player's hand
        drawn = self.deck.del_card()
        Player.hand.append(x)
        print drawn

    def discard(self):
        del Player.hand[int(raw_input("Which do you want to discard a card? ")) - 1]
        

x = Player()
x.draw()
x.discard()
x.show_hand()
