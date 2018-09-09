# -*- coding: utf-8 -*-

from GameScreen import *
from sense_hat import SenseHat

if __name__ == '__main__':
    # Initialize the sense hat
    sense = SenseHat()
    # Enable the accelerometer only
    # 1: compass 2: gyroscope 3: accelerometer
    sense.set_imu_config(False, False, False)
    # Enable the low light mode
    sense.low_light = True
    # Clean the screen
    sense.clear()
    # Initialize the main game screen
    gameScreen = GameScreen(sense)
    try:
        # Launch the main loop
        gameScreen.run()
    except KeyboardInterrupt:
        print("\n[Info]: The game was closed.\n")
