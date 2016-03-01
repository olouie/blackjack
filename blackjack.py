import random

class Deck(object):
    
    # A deck needs 52 cards, consisting of 13 ranks of 4 different suits
    # Perhaps these should be tuples
     
    suits = ('hearts', 'spades', 'diamonds', 'clubs')
    ranks = {'ace':11, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 
             'ten':10, 'jack':10, 'queen':10, 'king':10}  
    
    stack = {}
    
    for suit in suits:
        for k,v in ranks.iteritems():
            stack[k + ' of ' + suit] = v
    
    def __init__(self):
        print 'Deck has been created!'

    def deck_total(self): # Displays total cards remaining
        print "There are %d cards left in this deck." %len(self.stack)

    def random_card(self): # Chooses one card at random
        card = random.choice(self.stack.keys())
        print card

x = Deck()
x.deck_total()