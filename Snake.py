# -*- coding: utf-8 -*-

from Direction import *
from Map import *
from Point import *


class Snake(object):
    """
    Snake
    A Snake object
    """

    def __init__(self, size, mappy):
        """
        Initialize the Snake
        :param size The size of the Snake
        :param mappy A map
        """
        self.mappy = mappy
        self.direction = Direction()
        self.direction.direction = 0
        self.size = size
        self.speed = 1
        self.positions = []
        self.__generate__()

    def __str__(self):
        """
        Return a string representation of the Snake
        :return A string representation of the Snake
        """
        string = 'Snake: '
        for i in self.positions:
            string += str(i) + " "
        string += "\n"
        return string

    def __generate__(self):
        """
        Generate the body of the Snake
        """
        # Append the head to the positions table
        self.positions.append(Point(2, 5))
        # Generate the body of the Snake
        # Body = size - 2 because I start at 0 index and I remove the head that
        # is already generate
        # The position of a part of the body of the Snake
        x = 0
        y = 0
        direction = 2
        for i in range(0, self.size - 1):
            if (direction == 0 and self.positions[i].y > 0):
                x = self.positions[i].x
                y = self.positions[i].y - 1
                if (y <= 0):
                    direction = 2
            elif (direction == 1 and
                    self.positions[i].x < self.mappy.max):
                x = self.positions[i].x + 1
                y = self.positions[i].y
                if (y >= self.mappy.max):
                    direction = 0
            elif (direction == 2 and
                    self.positions[i].y < self.mappy.max):
                x = self.positions[i].x
                y = self.positions[i].y + 1
                if (y >= self.mappy.max):
                    direction = 1
            elif (direction == 3 and self.positions[i].x > 0):
                x = self.positions[i].x - 1
                y = self.positions[i].y
            self.positions.append(Point(x, y))

    def move(self):
        """
        Move the Snake
        """
        direction = self.direction.direction
        x = 0
        y = 0
        for i in range(self.size - 1, 0, -1):
            posTemp = self.positions[i]
            self.positions[i] = self.positions[i - 1]
            self.positions[i - 1] = posTemp
        if (direction == 0):
            x = self.positions[1].x
            y = self.positions[1].y - 1
        elif (direction == 1):
            x = self.positions[1].x + 1
            y = self.positions[1].y
            if (y >= self.mappy.max):
                direction = 0
        elif (direction == 2):
            x = self.positions[1].x
            y = self.positions[1].y + 1
            if (y >= self.mappy.max):
                direction = 1
        elif (direction == 3):
            x = self.positions[1].x - 1
            y = self.positions[1].y
        self.positions[0] = Point(x, y)

    def turn(self, direction):
        """
        Change the direction of the snake
        :param direction The new direction of the Snake
        """
        if (direction == 0):
            x = self.positions[0].x
            y = self.positions[0].y - 1
        elif (direction == 1):
            x = self.positions[0].x + 1
            y = self.positions[0].y
        elif (direction == 2):
            x = self.positions[0].x
            y = self.positions[0].y + 1
        elif (direction == 3):
            x = self.positions[0].x - 1
            y = self.positions[0].y

        if (self.positions[1].x == x and self.positions[1].y == y):
            canChangeDirection = False
        else:
            canChangeDirection = True

        if (canChangeDirection):
            self.direction.direction = direction

    def update(self, delta):
        """
        Update the Snake
        :param delta The mother delta
        :return A boolean that is True when the snake is dead
        """
        self.move()
        return self.__isDead__()

    def __isDead__(self):
        """
        Detect if the snake is dead
        :return A boolean that is True when the snake is dead
        """
        if (self.positions[0].x < self.mappy.min or
            self.positions[0].x > self.mappy.max or
            self.positions[0].y < self.mappy.min or
                self.positions[0].y > self.mappy.max):
            return True
        return False
