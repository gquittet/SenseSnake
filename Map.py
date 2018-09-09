# -*- coding: utf-8 -*-


class Map(object):
    """
    Map
    A simple square map
    """

    def __init__(self, min, max):
        """
        Generate the map
        :param min The minimum size of the map
        :param max The maximum size of the map
        """
        self.min = min
        self.max = max
