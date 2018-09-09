# -*- coding: utf-8 -*-


class InputHandler(object):
    """
    Need for the linking with the joystick
    """

    def __init__(self, gameWorld):
        """
        Initialize an InputHandler
        :param sense The sense hat
        :param gameWorld The gameWorld
        """
        self.snake = gameWorld.snake
        self.stick = gameWorld.sense.stick
        self.__initStick__()

    def __initStick__(self):
        """
        Initialize the functions of the joystick
        """
        self.stick.direction_up = self.onPushUp
        self.stick.direction_right = self.onPushRight
        self.stick.direction_down = self.onPushDown
        self.stick.direction_left = self.onPushLeft

    def onPushUp(self):
        """
        Detect the joystick move to up
        """
        self.snake.turn(0)

    def onPushRight(self):
        """
        Detect the joystick move to right
        """
        self.snake.turn(1)

    def onPushDown(self):
        """
        Detect the joystick move to down
        """
        self.snake.turn(2)

    def onPushLeft(self):
        """
        Detect the joystick move to left
        """
        self.snake.turn(3)
