

from time import sleep 
from adafruit_circuitplayground import cp

while True:
    light = cp.light
    if light % 32 == 0 and cp.light !=0:
        light = light - 1 
    index = light // 32
    if light > 32:
        light = light - (index * 32)
    for i in range(0, 10):
        if i == index :
             color = int(255 * light  / 32)
             print(color)
             cp.pixels[i] = (color, color, color)    
        elif i > index:
            cp.pixels[i]= 0
        else:
            cp.pixels[i] = 1

    