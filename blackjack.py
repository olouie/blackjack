import random
#import os
#os.system('clear')

class Deck(object):
    
    # A deck needs 52 cards, consisting of 13 ranks of 4 different suits
     
    suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
    ranks = {'Ace':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 
            'Jack':10, 'Queen':10, 'King':10}  
    
    stack = {}
    untouched_stack = {}
    
    for suit in suits:
        for k,v in ranks.iteritems():
            stack[k + ' of ' + suit] = v
            untouched_stack[k + ' of ' + suit] = v
    
    def __init__(self):
        print 'Welcome to Blackjack'

    def deck_total(self): 
    # Displays total cards remaining
        print "There are %d cards left in this deck" %len(self.stack)

    def random_card(self): 
    # Chooses one card at random
        card = random.choice(self.stack.keys())
        return card

    def del_card(self):
        # Deletes card chosen at random
        x = self.random_card()
        self.stack.pop(x)
        return x


class Bank(object):

    # Bank will hold as Player's money and earnings

    bank = 100
    betting_box = 0

    def __init__(self):
        #print "Bank is running"
        pass

    def bank_total(self):
        print Player.name, 'has', '$'+str(Bank.bank), 'in their bank'

    def betting_box_total(self):
        print 'There is', '$'+str(self.betting_box), 'in', Player.name+'s','betting box'

    def bet(self):
        self.bank_total()
        while True:
            try:
                wager = int(raw_input("How much would you like to bet? "))
            except:
                print 'Please enter an integer'
            else:
                while True:
                    if wager > self.bank:
                        print 'You cannot bet more than what you have in your bank'
                    elif wager <= self.bank:
                        print Player.name, 'has wagered', '$'+str(wager)
                        Bank.bank -= wager
                        self.betting_box += wager
                        self.betting_box_total()
                        break
                break

    def bet_win(self):
        Bank.bank += self.betting_box
        self.betting_box = 0
        self.betting_box_total()


class Player(Deck, Bank):

    # A player should be dealt 2 cards at random, surrender hand

    hand = ['Ace of Hearts', 'Jack of Hearts']
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
    # No splitting of hands in this game
    
    def __init__(self):
        self.player = Player()
        self.bank = Bank()
        #print "Game engine running"

    def play(self):
        while True:
            while self.bank.bank > 0:
                # Before a new round starts, checks bank. If bank == 0, game over           
                if self.bank.bank == 0:
                    print 'You have no more money left in your bank\nGame Over'
                    break

                # If deck is less than 2 cards no more can be dealt, then game over
                if len(self.stack) < 2:
                    print 'There are no more cards left in this deck\nGame Over'
                    break

                #self.player.deal()
                self.prompt()

            if not self.replay():
                print 'Thank you for playing Blackjack'
                break
            else:
                self.reset()

    def prompt(self):
        # Prompts the Player to Hit, Stand, or Surrender
        # Rearrange order of conditionals when game comes together more
        while True:
            self.bet()

            if self.win_loss() == True:
                print 'All wagers go to', self.player.name
                self.bet_win()
                break

            reply = raw_input("Would you like to: Hit, Stand, or Surrender\n").lower()

            if reply.startswith('h'):
                print self.player.name, 'drew a', self.player.draw()
                # Add the comparison here to see if player busts after a Hit
                self.show_hand()
            elif reply.startswith('st'):
                print self.player.name, 'stands hand'
                # This only matters when playing against Dealer
                # Add comparisons and then discard hand
                break
            elif reply.startswith('su'):
                # Player gets to withdraw wager, how the hell I'm supposed to do this ::cries::
                print self.player.name, 'surrendered their hand'
                self.player.discard_hand()
                break

    def win_loss(self):
        # Will add the values in Player's hand to see if win or loss
        # Aces have an optional value of 1 or 11
        card_values = {}

        for card in self.player.hand:
            card_values[card] = self.untouched_stack[card]

        if 11 in card_values.itervalues():
            ace_prompt = raw_input("Would you like your Ace to value 1? ").lower()
            if ace_prompt.startswith('y'):
                card_values[card_values.keys()[card_values.values().index(11)]] = 1
                print self.player.name+'s', 'Ace now equals 1'

        if sum(card_values.itervalues()) == 21:
            print self.player.name+'s', 'hand equals 21\n', self.player.name, 'wins this round'
            return True
        elif sum(card_values.itervalues()) > 21:
            print self.player.name+'s', 'hand is over 21\n', self.player.name, 'loses this round'
            return False

    def replay(self):
        return raw_input('If you like to play again, type "yes" and press enter.\n').lower().startswith('y')

    def reset(self):
        self.player = Player()
        self.bank = Bank()

x = Game()
x.bet()
