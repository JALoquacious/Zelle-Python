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

from random import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'X: {self.x:.2f}, Y: {self.y:.2f}'

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def is_inside_circle(self, radius):
        return self.x ** 2 + self.y ** 2 <= radius ** 2

    def is_bulls_eye(self):
        return self.x == 0 and self.y == 0

class Cabinet:
    def __init__(self, size):
        self.dimension = size
        self.radius = size / 2
        self.circle_hits = 0
        self.hits = 0

    def __str__(self):
        return (f'Hits inside circle: {self.circle_hits}, ' +
                f'Hits outside circle: {self.hits - self.circle_hits}')

    def throw(self, dart):
        if dart.is_inside_circle(self.radius):
            self.circle_hits += 1
        self.hits += 1

class Game:
    def __init__(self, size):
        self.cab = Cabinet(size)

    def simulate(self, num_darts):
        for i in range(num_darts):
            dart = Point(self.cab.dimension * random() - self.cab.radius,
                         self.cab.dimension * random() - self.cab.radius)
            print('DART:', dart, '| In circle?',
                  dart.is_inside_circle(self.cab.radius))
            self.cab.throw(dart)
        print(str(self.cab))

def main():
    game = Game(size = 100)
    game.simulate(100)


if __name__ == '__main__':
    main()
