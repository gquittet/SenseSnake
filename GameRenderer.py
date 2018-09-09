# -*- coding: utf-8 -*-


class GameRenderer(object):
    """
    GameRenderer
    The main game renderer that make the render of the game
    """

    def __init__(self, gameWorld):
        """
        Initialize the game renderer
        :param sense The sense hat
        :param gameWorld The GameWorld object
        """
        self.gameWorld = gameWorld
        self.sense = gameWorld.sense
        self.snake = gameWorld.snake
        self.mappy = gameWorld.mappy
        self.candy = gameWorld.candy
        self.mapToDraw = []

    def __renderSnake__(self):
        """
        Render the Snake
        """
        maximum = (self.mappy.max + 1) * (self.mappy.max + 1)
        # Make a matrix 1 x 64 with this content [0, 0, 0]
        for i in range(self.mappy.min, maximum):
                self.mapToDraw.append([0, 0, 0])
        # Change the tuple with a color. The indices are the position of the
        # Snake body
        for i in self.snake.positions:
            self.mapToDraw[i.y * (self.mappy.max + 1) + i.x] = [180, 180, 180]

    def __renderCandy__(self):
        """
        Render the Candy
        """
        c = self.candy
        self.mapToDraw[c.y * (self.mappy.max + 1) + c.x] = [255, 0, 0]

    def render(self):
        """
        The rendering of the game
        """
        self.mapToDraw = []
        self.__renderSnake__()
        self.__renderCandy__()
        self.sense.set_pixels(self.mapToDraw)
