import rgb
import board # pylint: disable=import-error
import time
from fancyLED import FancyLED
# led1 = rgb.RGB(board.D3, board.D4, board.D2)

fancy1 = FancyLED(board.D5, board.D6, board.D7)
fancy2 = FancyLED(board.D2, board.D3, board.D4)

while True:
    fancy1.alternate(.5, 5)

    fancy2.blink(.25, 5)

    for i in range(0, 5):
        fancy2.chase(.1, 1)
        fancy1.chase(.1, 1)

    for i in range(0, 100):
        fancy2.sparkle(.05, 2)
        fancy1.sparkle(.05, 2)