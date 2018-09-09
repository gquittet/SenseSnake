# -*- coding: utf-8 -*-

from GameWorld import *
from GameRenderer import *
from InputHandler import *
import time


class GameScreen(object):
    """
    GameScreen
    The main screen class
    """

    def __init__(self, sense):
        """
        Initialize the main game screen
        :param sense The sense hat
        """
        # Initialize the game world
        self.gameWorld = GameWorld(sense)
        # Initialize the game renderer
        self.gameRenderer = GameRenderer(self.gameWorld)
        # Initialize the input handler
        self.inputHandler = InputHandler(self.gameWorld)
        self.sense = sense

    def run(self):
        """
        Launch and run the game
        """
        # Run the loop
        running = True
        # Need for the updates limit
        # One second in nano second
        second = 1000000000
        beforeTime = time.clock() * second
        elapsedTime = 0
        ups = 60.0
        # The score
        score = 0
        # Need for the performance analyse
        timer = time.clock() * second
        updates = 0
        frames = 0
        while (running):
            if (elapsedTime > (second / ups)):
                running, score = self.gameWorld.update(elapsedTime)
                beforeTime = time.clock() * second
                updates += 1
            else:
                self.gameRenderer.render()
                frames += 1
            elapsedTime = (time.clock() * second) - beforeTime
            # Performace analyser
            timerShow = (time.clock() * second) - timer
            if (timerShow >= second):
                print("Time (s): " + str('%1d' % time.clock()) +
                      " | Timer (ns): " + str('%.4f' % timerShow) +
                      " | UPS: " + str(updates) + " | FPS: " + str(frames))
                timer = time.clock() * second
                updates = 0
                frames = 0
        print("\n[Info]: Game Over")
        print("[Info]: Score: " + str(score) + "\n")
        self.sense.clear()
        self.sense.show_message("Game Over", text_colour=[200, 0, 0])
        self.sense.clear()
        self.sense.show_message("Score: " + str(score),
                                text_colour=[180, 180, 180])
        self.sense.clear()
