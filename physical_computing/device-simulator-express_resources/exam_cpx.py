from adafruit_circuitplayground import cp
from time import sleep
num =1 
num2 = 1
index = 9; 
while True:
    cp.pixels[index]= 1
    sleep(1)
    cp.pixels[index] = 0
    if index == 9:
        cp.pixels[0] = 1
        cp.pixels[9] = 1
        sleep(1)
        cp.pixels[0] = 0
    elif index == 5:
        cp.pixels[4] = 1
        sleep(1)
        cp.pixels[4] = 0
    index = index - num 
    