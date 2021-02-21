from adafruit_clue import clue
from time import *

clue_data = clue.simple_text_display( text_scale=2)
clue_data[1].color = (255, 255,0)
clue_data[2].color = (255,255,0)
clue_data[4].color = (255,255,255)
clue_data[6].color = (255,0,255)
rightToLeft = "This message moves from right to left..."
leftToRight = "This message moves from left to right..."
while True:
    clue_data[0].text = "Message Streamer"
    clue_data[2].text = rightToLeft
    clue_data[4].text = leftToRight
    clue_data[6].text = "This message blinks"
    clue_data[6].color = (0,0,255)
    sleep(1)
    clue_data[6].color = (0,0,0)

    letterRight = rightToLeft [0:1]
    rightToLeft = rightToLeft[1:] + letterRight

    letterLeft = leftToRight [:-1]
    leftToRight = leftToRight[-1:] + letterLeft
    clue_data.show()