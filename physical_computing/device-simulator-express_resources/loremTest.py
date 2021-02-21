"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""
import time
# import CPX library
from adafruit_circuitplayground import cp

Long version
counter = 10
while True:    
    if cp.switch :
        counter = counter + 1
        if counter > 10 :
            counter = 0
    else:
        counter = counter - 1
        if counter < 0 :
            counter =  9
    cp.pixels[0] = 1 if counter == 0 else 0
    cp.pixels[1] = 1 if counter == 1 else 0
    cp.pixels[2] = 1 if counter == 2 else 0
    cp.pixels[3] = 1 if counter == 3 else 0
    cp.pixels[4] = 1 if counter == 4 else 0
    cp.pixels[5] = 1 if counter == 5 else 0
    cp.pixels[6] = 1 if counter == 6 else 0
    cp.pixels[7] = 1 if counter == 7 else 0
    cp.pixels[8] = 1 if counter == 8 else 0
    cp.pixels[9] = 1 if counter == 9 else 0
    
    time.sleep(1)


#short version
counter = 10
while True:
    if cp.switch :
        counter = counter + 1
        if counter > 10 :
            counter = 0
    else:
        counter = counter - 1
        if counter < 0 :
            counter =  9
    for i in range(0,10,1) :
        cp.pixels[i] = 1 if counter == i else 0
        
    time.sleep(1)

