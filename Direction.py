# -*- coding: utf-8 -*-

import random


class Direction(object):
    """
    Direction
    The Direction object
    """

    def __init__(self):
        """
        Initialize a direction
        """
        self.direction = 0

    def generate(self):
        """
        Update the direction as an Integer
        0 : up      1 : right
        2 : down    3 : left
        """
        self.direction = random.randint(0, 3)
