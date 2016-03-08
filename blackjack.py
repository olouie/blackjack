import random
#import os
#os.system('clear')

class Deck(object):
    
    # A deck needs 52 cards, consisting of 13 ranks of 4 different suits
     
    suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
    ranks = {'Ace':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 
            'Jack':10, 'Queen':10, 'King':10}  
    
    stack = {}
    
    for suit in suits:
        for k,v in ranks.iteritems():
            stack[k + ' of ' + suit] = v
    
    def __init__(self):
        print 'Welcome to Blackjack'

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
        #print "Bank is running"
        pass

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
    # Add class variable, Player's name

    hand = []
    name = ''

    def __init__(self):
        self.deck = Deck()
        #Player.name = raw_input("Player name: ")

    def show_hand(self):
        print Player.name, 'has a', ' and a '.join([str(x) for x in Player.hand] )

    def discard_hand(self):
        hand = []

    def draw(self):
        # Adds a randomly chosen card to Player's hand
        drawn = self.deck.del_card()
        Player.hand.append(drawn)
        return drawn

    def deal(self):
        # Deals 2 cards to Player
        print Player.name, 'was dealt a', self.draw(), 'and a', self.draw()


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
        #print "Game engine running"

    def play(self):
        while True:
            while len(self.stack) >= 2 or bank != 0:
                self.player.deal()
                self.prompt()

            if not self.replay():
                break

    def prompt(self):
        # Prompts the Player to Hit, Stand, or Surrender
        while True:
            reply = raw_input("Would you like to: Hit, Stand, or Surrender\n").lower()

            if reply.startswith('h'):
                print self.player.name, 'drew a', self.player.draw()
                self.show_hand()
            elif reply.startswith('st'):
                print self.player.name, 'stands hand'
                break
            elif reply.startswith('su'):
                print self.player.name, 'surrendered their hand'
                self.player.discard_hand()
                break


    def replay(self):
        return raw_input('Would you like to play again? ').lower().startswith('y')


x = Game()
x.play()
