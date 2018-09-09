# -*- coding: utf-8 -*-


class Score(object):
    """
    Score
    A simple score
    """

    def __init__(self):
        """
        Make a new Score
        """
        self.score = 0

    def increaseScore(self, n, level):
        """
        Increase the score with a value
        :param n The increase value
        :param level The current level state
        """
        speed = int(n.speed * 100)
        self.score = speed + (level.level * 5)
        n.speed += 0.1
