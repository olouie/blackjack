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


class Bank(object):
    # Bank will hold as Player's money and earnings
    # Player should be able to bet to the total of their bank
    # Pot will hold amounts betted by Player and Dealer
    # Pot will be added or subtracted from bank

    bank = 100
    pot = 0

    def __init__(self):
        print "Bank is running"

    def bank_total(self):
        print Bank.bank

    def pot_total(self):
        print Bank.pot

    def bet(self):
        # Fix later so Player cannot bet more than bank
        wager = int(raw_input("How much would you like to bet? "))
        Bank.bank -= wager
        Bank.pot += wager


class Player(Deck, Bank):

    # A player should be dealt 2 cards at random, have the ability to discard 1-2 cards, draw 1-2 cards at random
    # Create class variable to hold the hand of the player
    # Add class variable, Player's name?

    hand = []
    name = ''

    def __init__(self):
        self.deck = Deck()
        Player.name = raw_input("Player name: ")

    def show_hand(self):
        print Player.hand

    def draw(self):
        # Adds a randomly chosen card to Player's hand
        drawn = self.deck.del_card()
        Player.hand.append(drawn)
        return drawn

    def deal(self):
        # Deals 2 cards to Player
        print self.draw(), 'and', self.draw()

    def discard(self):
        # Fix this later for error and exceptions
        del Player.hand[int(raw_input("Which do you want to discard a card? ")) - 1]


class Game(Player):
    # Game engine that handles the logic and comparisons...maybe
    # Set up for one player first, add Dealer later (contemplate a Dealer class?)
    # If cards are 21, automatic win
    # If cards are over 21, automatic bust
    # No splitting of hands in this game
    # Replay? When no more can be dealt from a deck
    
    def __init__(self):
        self.player = Player()
        self.bank = Bank()
        print "Game engine running"

    def play(self):
        pass

    def replay(self):
        pass


x = Game()
print Player.name
