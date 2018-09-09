# -*- coding: utf-8 -*-

from Point import *
from random import *


class Candy(object):
    """
    Candy
    A candy that feed the Snake
    """

    def __init__(self, snake):
        """
        Make a Candy
        :param snake The snake
        """
        self.snake = snake
        self.randomize()

    def randomize(self):
        """
        Generate the candy position
        """
        self.x = randint(self.snake.mappy.min, self.snake.mappy.max)
        self.y = randint(self.snake.mappy.min, self.snake.mappy.max)
        while (self.__isInSnake__()):
            self.x = randint(self.snake.mappy.min, self.snake.mappy.max)
            self.y = randint(self.snake.mappy.min, self.snake.mappy.max)

    def __isInSnake__(self):
        """
        Check if the current position isn't in the body of the Snake
        """
        for i in self.snake.positions:
            if (self.x == i.x and self.y == i.y):
                return True
        return False
