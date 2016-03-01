class Deck(object):
    
    # A deck needs 52 cards, consisting of 13 ranks of 4 different suits
    # Perhaps these should be tuples
     
    suits = ('hearts', 'spades', 'diamonds', 'clubs')
    ranks = {'ace':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 
             'ten':10, 'jack':10, 'queen':10, 'king':10}  
    
    stack = {}
    
    for suit in suits:
        for k,v in ranks.iteritems():
            stack[k + ' of ' + suit] = v
    
    def __init__(self):
        print self.stack

x = Deck()