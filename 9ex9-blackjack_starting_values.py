# Chapter 9 - Exercise 9
# A blackjack dealer always starts with one card showing. It would be useful for
# a player to know the dealer’s bust probability (see previous problem) for each
# possible starting value. Write a simulation program that runs multiple hands
# of blackjack for each possible starting value (ace–10) and estimates the
# probability that the dealer busts for each starting value.

import random

class Card:
    __units = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
               'T':10, 'J':10, 'Q':10, 'K':10}
    
    def __init__(self, name):
        if (name in Card.__units):
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
    def play(self):
        deck = Deck()
        dealer = 0

        while dealer <= 17:
            card = deck.random_card()
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
