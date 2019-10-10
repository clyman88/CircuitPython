# importing necessary libraries
import board
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull
'''from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode'''

# importing the sensor library
from adafruit_hcsr04 import HCSR04

#declaring dot and sensor (not lcd apparently because there isn't enough memory. Apparently.)

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
# lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
sensor = HCSR04(board.D6, board.D5)

# not useless variables this time for r, g, b values for neopixel
r = 255
g = 0
b = 0

# distance variable
dist = 0

while True:
    #filling the neopixel with r, g, b variables
    dot.fill((r, g, b))

    # COLOR CODE

    # r is decreasing by increments of 17 dependent on the distance since 255/15 = 17,
    # evenly changing the color as the distance increases
    if dist <=15:
        r = 255-(17*dist)
        b = 0+(17*dist)
        g = 0
    # very similar to if statement ^^^, essentially the same but with blue and green
    elif dist > 15:
        b = 255-(17*(dist-15))
        g = 0+(17*(dist-15))
        r = 0

    # making sure no errors will be thrown if the r, g, or b values are out of range
    if r <=0:
        r = 0
    if b >= 255:
        b = 255
    if b <= 0:
        b = 0
    if g >= 255:
        g = 255

    # library says that if the distance is too far or is having trouble, it will throw
    # a RuntimeError - by using try and except, the program will not halt if a 
    # RuntimeError occurs (because there is a pass statement)
    try:
        dist = int(sensor.distance)

    except RuntimeError:
        pass

    #self-explanatory

    print("The distance is " + str(dist))

    time.sleep(.1)
