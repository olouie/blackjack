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

    bank = 5
    pot = 0

    def __init__(self):
        #print "Bank is running"
        pass

    def bank_total(self):
        print Player.name, 'has', '$'+str(Bank.bank), 'in their bank'

    def pot_total(self):
        print 'There is', '$'+str(Bank.pot), 'in the pot'

    def bet(self):
        while True:
            wager = int(raw_input("How much would you like to bet? "))
            if wager > Bank.bank:
                print 'You cannot bet more than what you have in your bank'
            elif wager <= Bank.bank:
                print Player.name, 'has wagered', '$'+str(wager)
                Bank.bank -= wager
                Bank.pot += wager
                self.pot_total()
                break


class Player(Deck, Bank):

    # A player should be dealt 2 cards at random, surrender hand

    hand = []
    name = ''

    def __init__(self):
        self.deck = Deck()
        #Player.name = raw_input("Player name: ")

    def show_hand(self):
        Player.hand.sort()
        print Player.name, 'has in hand:\n -', '\n - '.join([str(x) for x in Player.hand] )

    def discard_hand(self):
        # When a hand is surrendered
        Player.hand = []

    def draw(self):
        # Adds a randomly chosen card to Player's hand
        drawn = self.deck.del_card()
        Player.hand.append(drawn)
        return drawn

    def deal(self):
        # Deals 2 cards to Player
        print Player.name, 'was dealt:\n - ', self.draw(), '\n - ', self.draw()


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
            while self.bank.bank > 0:
                self.player.deal()
                self.prompt()

                # If deck is less than 2 cards no more can be dealt, then game over
                if len(self.stack) < 2:
                    break

            if not self.replay():
                print 'Thank you for player Blackjack'
                break

    def prompt(self):
        # Prompts the Player to Hit, Stand, or Surrender
        # Rearrange order of conditionals when game comes together more
        while True:
            reply = raw_input("Would you like to: Hit, Stand, or Surrender\n").lower()

            if reply.startswith('h'):

                # Prevents player from drawing more cards from empty deck, game over
                if len(self.stack) < 2:
                    break

                print self.player.name, 'drew a', self.player.draw()
                # Add the comparison here to see if player busts after a Hit
                self.show_hand()
                self.bank.bank -= 1

                if self.bank.bank == 0:
                    break
            elif reply.startswith('st'):
                print self.player.name, 'stands hand'
                # This only matters when playing against Dealer
                # Add comparisons and then discard hand
                break
            elif reply.startswith('su'):
                print self.player.name, 'surrendered their hand'
                self.player.discard_hand()
                break


    def replay(self):
        return raw_input('If you like to play again, type "yes" and press enter.\n').lower().startswith('y')


x = Game()
x.play()
