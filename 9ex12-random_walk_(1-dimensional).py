# Chapter 9 - Exercise 12
# A random walk is a particular kind of probabilistic simulation that models
# certain statistical systems such as the Brownian motion of molecules. You can
# think of a one-dimensional random walk in terms of coin flipping. Suppose you
# are standing on a very long straight sidewalk that extends both in front of
# and behind you. You flip a coin. If it comes up heads, you take a step
# forward; tails means to take a step backwards.

# Suppose you take a random walk of n steps. On average, how many steps away
# from the starting point will you end up? Write a program to help you
# investigate this question.

from random import choice

def walk(steps):
    values = []
    for s in range(steps):
        values.append(choice([-1, 1]))
    return sum(values)

def simulate(walks, steps):
    total = 0
    for i in range(walks):
        distance = walk(steps)
        total += distance
        print(f'Sim # {i + 1:3d}:\t\t{distance:5d} steps')
        print('-----------------------------------')
    print('Average movement from starting position:', total / walks)

def main():
    simulate(walks = 10, steps = 10000) # high lag with steps > 500,000

if __name__ == '__main__':
    main()
