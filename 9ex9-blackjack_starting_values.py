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
    
    def play(self, starting_value):
        dealer = starting_value
        while dealer <= 17:
            card = self.deck.random_card()
            if card.is_ace():
                if 17 <= dealer + 11 <= 21:
                    card.value += 10
            dealer += card.value
        return True if dealer > 21 else False

    def cycle(self, games):
        low = float('inf')
        high = float('-inf')
        low_card, high_card = 0, 0
        for card in self.deck.cards[:10]:
            busts = 0
            init_val = Card(card).value
            for i in range(games):
                busts += self.play(init_val)
            score = busts / games
            edge = (.5 - score) * 100
            if edge < low:
                low = edge
                low_card = card
            if edge > high:
                high = edge
                high_card = card
            print_results(card, busts, games, score, edge)
        return low, high, low_card, high_card

def print_results(card, busts, games, score, edge):
    perf = 'better' if edge >= 0 else 'worse'
    print(f'When initial card is {card}, ', end='')
    print(f'dealer busts in {busts} out of {games} games ({score:.3f}%)')
    print(f'The house should perform about {edge:.2f}% {perf} than random.\n')

def print_summary(low, high, low_card, high_card):
    print(f'The dealer performs worst ({low:.2f}%) when initial draw is ' +
          f'{low_card}.')
    print(f'The dealer performs best ({high:.2f}%) when initial draw is ' +
          f'{high_card}.')

def main():
    blackjack = Game()
    low, high, low_card, high_card = blackjack.cycle(10000)
    print_summary(low, high, low_card, high_card)

    
if __name__ == '__main__':
    main()
