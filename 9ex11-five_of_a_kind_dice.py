# Chapter 9 - Exercise 11
# Write a program that performs a simulation to estimate the probability of
# rolling five-of-a-kind in a single roll of five six-sided dice.

# Author's note:
# I understand this problem can be done much more efficiently without
# the use of classes and expensive instantiation. In fact, a single function
# with a loop should be all it takes. Also, static classes and fields are not
# very 'pythonic.' However, I've deliberately over-modeled things here to help
# translate my C# OOP experience to Python. Right now this is more about having
# fun with object-oriented modeling than obsessive efficiency.

from random import random
from math import ceil

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.value = ceil(random() * sides)

    def __str__(self):
        return (f'This {self.sides}-sided dice has a current face value of ' +
                f'{self.value}.')

    def __lt__(self, other): return self.value < other.value
    def __gt__(self, other): return self.value > other.value
    def __le__(self, other): return self.value <= other.value
    def __ge__(self, other): return self.value >= other.value
    def __eq__(self, other): return self.value == other.value


class Sim(object):
    DIE_SIDES = 6
    DIE_COUNT = 5
    
    @staticmethod
    def run(iterations):
        jackpots = 0
        for i in range(iterations):
            dice = [Die(Sim.DIE_SIDES) for i in range(Sim.DIE_COUNT)]
            if all(d == dice[0] for d in dice):
                # print([d.value for d in dice]) # DEBUG
                jackpots += 1
        return jackpots, iterations


def print_summary(jackpots, iterations):
    percentage = jackpots / iterations * 100
    print(f'{jackpots} jackpots were hit out of {iterations} iterations.')
    print(f'Probability of success for {Sim.DIE_COUNT} {Sim.DIE_SIDES}-sided ' +
          f'dice to roll the same value is {percentage:.2f}%')

def main():
    print_summary(*Sim.run(10000))

if __name__ == '__main__':
    main()
