from microbit import *
from time import sleep
from adafruit_clue import clue
clue_data = clue.simple_text_display(title= "", text_scale= 2, )
message = "This is a message."
while True:
    clue_data[2].text = message
    clue_data[2].color = clue.AQUA
    sleep(1)
    clue_data[2].color = clue.BLACK
    sleep(0.5)
    clue_data.show()
    removeLetter = message [0]
    message = message [1:] + removeLetter
    