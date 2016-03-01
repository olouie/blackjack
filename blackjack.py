import random

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
        print "There are %d cards left in this deck." %len(self.stack)

    def random_card(self): 
    # Chooses one card at random
        card = random.choice(self.stack.keys())
        return card

    def del_card(self):
        # Deletes card chosen at random
        x = self.random_card()
        return x
        self.stack.pop(x)

class Player(Deck):

    # A player should be dealt 2 cards at random, have the ability to discard 1-2 cards, draw 1-2 cards at random
    # Splitting a hand will not be in this time
    # If over 21, then automatic bust

    def deal(self):
        print 'Player drew a', self.del_card(), 'and a', self.del_card()

x = Player()
x.deck_total()
x.deal()
x.deck_total()