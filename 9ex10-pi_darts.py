# Chapter 9 - Exercise 10
# Monte Carlo techniques can be used to estimate the value of pi. Suppose you
# have a round dart board that just fits inside of a square cabinet. If you
# throw darts randomly, the proportion that hit the dart board vs. those that
# hit the cabinet (either on the board or in the corners not covered by the
# board) will be determined by the relative area of the dart board and the
# cabinet. If "n" is the total number of darts randomly thrown (that land
# within the confines of the cabinet), and "h" is the number that hit the board,
# it is easy to show that pi is approximately equal to 4(h/n).

# Write a program that accepts the "number of darts" as an input and then
# performs a simulation to estimate pi. Hint: you can use 2*random()-1 to
# generate the x and y coordinates of a random point inside a 2x2 square
# centered at (0,0). The point lies inside the inscribed circle if
# x**2 + y**2 <= 1.

import random

def main():
    simulate(num_darts)

def simulate(num_darts):
    pass

if __name__ == '__main__':
    main()
