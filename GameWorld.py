# -*- coding: utf-8 -*-

from Candy import *
from Level import *
from Map import *
from Score import *
from Snake import *


class GameWorld(object):
    """
    GameWorld
    The game world
    """

    def __init__(self, sense):
        """
        Initialize the game world
        :param sense The sense hat
        """
        self.level = Level()
        self.score = Score()
        self.mappy = Map(0, 7)
        self.snake = Snake(3, self.mappy)
        self.candy = Candy(self.snake)
        self.sense = sense
        self.i = 0
        print(self.snake)
        self.sense.clear()
        self.sense.show_message("Level: " + str(self.level.level),
                                text_colour=[180, 180, 180])

    def update(self, delta):
        """
        Compute all the objects
        :param delta The loop delta
        :return The dead state of the snake
        :return The score
        """
        deadStatus = False
        # UPS: 60 -> 2 * 60 = 120
        if (self.i >= (1.0 / self.snake.speed) * 120):
            deadStatus = self.snake.update(delta)
            self.__isEating__()
            print(self.snake)
            self.i = 0
        else:
            self.i += 1
        return (not deadStatus, self.score.score)

    def __isEating__(self):
        """
        Detect when the Snake eat a candy
        """
        head = self.snake.positions[0]
        if (head.x == self.candy.x and head.y == self.candy.y):
            self.score.increaseScore(self.snake, self.level)
            speed = int(self.snake.speed * 10)
            if (speed % 10 == 0):
                self.level.level += 1
                self.sense.clear()
                self.sense.show_message("Level: " + str(self.level.level),
                                        text_colour=[180, 180, 180])
                self.sense.clear()
                self.sense.show_message("Score: " + str(self.score.score),
                                        text_colour=[180, 180, 180])
                self.sense.clear()
            self.candy.randomize()
