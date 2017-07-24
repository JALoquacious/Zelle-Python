# Chapter 9 - Exercise 8
# Blackjack (twenty-one) is a casino game played with cards. The goal of the
# game to draw cards that total as close to 21 points as possible without going
# over. All face cards count as 10 points, aces count as 1 or 11, and all other
# cards count their numeric value.

# The game is played against a dealer. The player tries to get closer to 21
# (without going over) than the dealer. If the dealer busts (goes over 21) the
# player automatically wins (provided the player had not already busted). The
# dealer must always take cards according to a fixed set of rules. The dealer
# takes cards until he or she achieves a total of at least 17. If the dealer's
# hand contains an ace, it will be counted as 11 when that results in a total
# between 17 and 21 inclusive; otherwise, the ace is counted as 1.

# Write a program that simulates multiple games of blackjack and estimates the
# probability that the dealer will bust. Hints: treat the deck of cards as
# infinite. You do not need to keep track of the cards in the hand, just the
# total so far (treating an ace as 1) and a bool variable hasace that tells
# whether or not the hand contains an ace. A hand containing an ace should have
# 10 points added to the total exactly when doing so would produce a stopping
# total(something between 17 and 21 inclusive).

import random

class Card:
    __units = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
               'T':10, 'J':10, 'Q':10, 'K':10}
    
    def __init__(self, name):
        if name in Card.__units:
            self.name = name
            self.value = Card.__units[name]
        else:
            raise ValueError(name + ' is not a valid card.')

    def __str__(self):
        return self.name + ': ' + str(self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def is_ace(self):
        return self.name == 'A'

class Deck:
    def __init__(self):
        self.cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                      'T', 'J', 'Q', 'K']

    def __str__(self):
        return str(self.cards)
    
    def random_card(self):
        return Card(random.choice(self.cards))
    
class Game:
    def __init__(self):
        self.deck = Deck()
        
    def play(self):
        dealer = 0
        while dealer <= 17:
            card = self.deck.random_card()
            if card.is_ace():
                if 17 <= dealer + 11 <= 21:
                    card.value += 10
            dealer += card.value
        return True if dealer > 21 else False

def print_summary(busts, games):
    score = (.5 - busts / games) * 100
    perf = 'better' if score > 0 else 'worse'
    
    print(f'Dealer busts in {busts} out of {games} games ({busts/games:.3f}%)')
    print(f'The house should perform about {score:.2f}% {perf} than random.')

def main():
    blackjack = Game()
    games = 10000
    busts = 0
    for i in range(games):
        busts += blackjack.play()
    print_summary(busts, games)
    
if __name__ == '__main__':
    main()
