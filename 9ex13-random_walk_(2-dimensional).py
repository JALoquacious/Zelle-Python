# Chapter 9 - Exercise 13
# Suppose you are doing a random walk (see previous problem) on the steps of a
# city street. At each "step" you choose to walk one block (at random) either
# forward, backward, left, or right. In n steps, how far do you expect to be
# from the starting point? Write a program to help answer this question.

from random import choice

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'X: {self.x}'.ljust(8) + f'Y: {self.y}'


def main():
    pass

if __name__ == '__main__':
    main()
