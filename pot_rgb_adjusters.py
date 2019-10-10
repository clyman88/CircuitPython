# importing necessary libraries
import board
import neopixel
import time
from analogio import AnalogIn

# declaring potentiometers as AnalogIn objects
potentiometer1 = AnalogIn(board.A1)
potentiometer2 = AnalogIn(board.A2)
potentiometer3 = AnalogIn(board.A3)

# declaring dot as a NeoPixel object
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:

    # "mapping" potentiometer values to 0 to 255 so that they can be used
    # for r, g, b values
    pot_value1 = potentiometer1.value * .00389194139
    pot_value2 = potentiometer2.value * .00389194139
    pot_value3 = potentiometer3.value * .00389194139

    # filling dot with potentiometer values
    dot.fill((int(pot_value1), int(pot_value2), int(pot_value3)))
