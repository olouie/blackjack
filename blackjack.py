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
        hand = []
        dealer_hand = []

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

    def __init__(self):
        player_bank = 100
        player_betting_box = 0

        dealer_bank = 100
        dealer_betting_box = 0

    def bank_total(self, name, bank):
        print name, 'has', '$'+str(bank), 'in their bank'

    def betting_box_total(self, name, box):
        print 'There is', '$'+str(box), 'in', name+'\'s','betting box'

    def bet(self):
        # This method will not apply to Dealer, will get own bet for logic stuff
        self.bank_total(Player.name, Bank.player_bank)
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
                        Bank.player_bank -= wager
                        Bank.player_betting_box += wager
                        self.betting_box_total(Player.name, Bank.player_bank)
                        break
                break

    def bet_withdraw(self):
        # Dealer does not get to withdraw bet
        Bank.bank += self.betting_box
        self.betting_box = 0
        print Player.name, 'withdraws their wager'

    def bet_win(self, winner, winner_bank, winner_box):
        # Fix this so it's Player specfic so winnings go to correct Player
        winner_bank += Bank.player_betting_box +  Bank.dealer_betting_box
        winner_box = 0

    def bet_lose(self, box):
        # Set box to the the betting box of the loser
        box = 0

class Player(object):

    # A player should be dealt 2 cards at random, surrender hand

    # Move this class variables into the __init__()

    def __init__(self):
        name = 'Jack'
        dealer = 'Dealer'
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


class Dealer(Player):
    pass


class Game(object):
    # Game engine that handles the logic and comparisons...maybe
    # Set up for one player first, add Dealer later (contemplate a Dealer class?)
    # No splitting of hands in this game
    
    def __init__(self,):
        deck = Deck()
        bank = Bank()
        player = Player()
        dealer = Dealer()


    def play(self):
        while True:
            while self.bank > 0:
                # Before a new round starts, checks bank. If bank == 0, game over           
                if self.bank == 0:
                    print 'You have no more money left in your bank\nGame Over'
                    break

                # If deck is less than 2 cards no more can be dealt, then game over
                if len(self.stack) < 2:
                    print 'There are no more cards left in this deck\nGame Over'
                    break

                #self.player.deal()
                #self.prompt()
                print self.player.stack
                break

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
            elif self.win_loss() == False:
                print 'All wagers go to Dealer'
                # Betting boxes go to dealer
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
                self.bet_withdraw()
                self.player.discard_hand()
                break

    def win_loss(self):
        # Will add the values in Player's hand to see if win or loss
        # Aces have an optional value of 1 or 11
        # Have not incorporated the situation of multiple aces
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

# Do not need inheritence to use methods within class
# Create Dealer class

