import random
from datetime import datetime
random.seed(datetime.now())
####################################

class blackjack:
    def __init__(self):
        self.deck = [] # Deck
        self.suit = ['♠','♥','♦','♣']
        self.cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        self.dValue = 0 #summer will return to these Value functions
        self.pValue = 0
        self.dStand = False
        self.dTurn = False

    # for every suit and every card, append and randomize
    def setup(self):

        self.pHand = [] # Player hand
        self.dHand = [] # Dealer hand

        #Shuffling
        for s in self.suit:
            for c in self.cards:
                self.deck.append(str(c)+s)
        random.shuffle(self.deck)

        # Deals cards from last 4 cards in deck
        for i in range(2): #Append cards to dealer hand
            self.dHand.append(self.deck.pop())

        for i in range(2): #Append cards to player hand
            self.pHand.append(self.deck.pop())
        self.display()

    #Deals single cards
    def deal(self, hand):
        hand.append(self.deck.pop())
        self.display()

    def display(self): #Displays both players hands
        dPrint = []
        print('\nDealers Hand')
        self.dValue = self.summer(self.dHand)
        for i in range(len(self.dHand)):
            if i == 1: dPrint.append('?')
            else: dPrint.append(self.dHand[i])
        print(*dPrint)
       # print(self.dHand[0],'?')

        print('Players Hand')
        self.pValue = self.summer(self.pHand)
        print(*self.pHand, '({})'.format(self.pValue))

    # Converts face cards to numbers and sums.
    def summer(self, hand):
        holder = [] #holds the cards as strings to test
        value = 0 #holds the value of cards
        ace = 0
        for i in hand: #for card in hand, append number or face part, remove suit
            holder.append(i[:-1]) #append to holder
        for i in holder: #for every card in holder, test if JQK or A and add to value
            if i in 'JQK':
                value += 10
            elif i in 'A':
                value += 11
                ace += 1 #Adds ace to counter
            else: value += int(i)
        if value > 21 and ace > 0: # Ace checker
            value -= 11
            value += 1
        return(value)

    def turn(self):
        choice = input("\nWould you like to (h)it or (s)tand? ").lower()
        while choice not in 'hs':
            choice = input("\nWould you like to (h)it or (s)tand? ").lower()
        if choice == 'h':
            print('\n**Hit me!**')
            self.deal(self.pHand)
            self.pValue = self.summer(self.pHand)
            self.dTurn = True
            self.checker()

        else:
            print('\n**STAND**')
            self.ai()
            if self.dStand == True:
                self.checker()

    def checker(self):
        if self.dStand == True:
            if self.pValue > self.dValue:
                print('\nPlayer wins with',self.pValue, 'Dealer had',self.dValue)
                return(0)
            elif self.pValue < self.dValue:
                print('\nDealer wins with',self.dValue)
                return(0)
            else:
                print('\nPush')
        elif self.pValue == 21 and self.dValue == 21:
            print('\nPush')
            return(0)
        elif self.pValue == 21:
            print('\nPlayer Blackjack!')
            return(0)
        elif self.dValue == 21:
            print('\nDealer Blackjack!')
            return(0)
        elif self.dValue > 21:
            print('\nDealer Busts with', self.dValue)
            return(0)
        elif self.pValue > 21:
            print('\nPlayer Busts with', self.pValue)
            return(0)
        elif self.dTurn == True:
            self.dTurn = False
            self.ai()
            self.turn()
        else: self.turn()

    def ai(self):
        if self.dValue < 17:
            print('\n**Dealer hits**')
            self.deal(self.dHand)
            self.checker()
        elif 17 <= self.dValue <= 20:
            print('\n**Dealer stands**')
            self.dStand = True
            self.display()



    # Runs the game
    def game(self):
        self.setup()
        self.checker() #Initial check, players turn if no events

while True:
    reset = blackjack()
    reset.game()
    restart = input('\nWould you like to restart? Y/N ').lower()
    while restart not in 'yn':
        restart = input('\nWould you like to restart? Y/N ').lower()
    if restart == 'y':
        print("********RESTARTING********")
        continue
    else:
        break
