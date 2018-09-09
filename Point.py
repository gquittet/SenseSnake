# -*- coding: utf-8 -*-


class Point(object):
    """
    Point
    A simple 2D point
    """

    def __init__(self, x, y):
        """
        Initialize a point
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a string representation of a Point
        :return A string representation of a Point
        """
        return "[" + str(self.x) + ", " + str(self.y) + "]"
