# importing necessary libraries
import board
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

# declaring photointerrupter as a DigitalInOut object
pi = DigitalInOut(board.D6)
pi.direction = Direction.INPUT
pi.pull = Pull.UP

# declaring the dot as the neopixel on the board and lcd as LCD object
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

# semi-useless variables for r, g, b values for neopixel
r = 255
g = 0
b = 0

# happy and fun toggles for photointerrupter and time (elaborated on more)
toggle = True
time_toggle = True

# declaring current_time as a variable and declaring interrupts (variable being displayed
# on the lcd
current_time = 0

interrupts = 0

while True:
    dot.fill((r, g, b))

    # increasing interrupts when pi gets a value of True, setting toggle to False
    # so that this if statement will only run once per interrupt
    if pi.value and toggle:
        interrupts += 1
        g = 255
        r = 0
        toggle = False

    # changing neopixel color and setting toggle to True so that the if statement ^^^
    # can run again
    if not pi.value:
        r = 255
        g = 0
        toggle = True

    # FUN TIME TIME

    # if the time_toggle variable is True, run this statement
    if time_toggle:
        current_time = time.time() # setting current_time variable as time.time(), a variable that returns the seconds since some event
				   # important part - the variable increases by one every second
        time_toggle=False # so that this statement only runs once per every four seconds
        lcd.print("Number of")
        lcd.set_cursor_pos(1,0)
        lcd.print("Interrupts: " + str(interrupts))

    # will run if the current time is four less than the current time
    if current_time == time.time()-4:
        time_toggle = True # so that the if statement ^^^ can run again
        lcd.clear()
