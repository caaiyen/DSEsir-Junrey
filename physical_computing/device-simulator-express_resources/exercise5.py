from microbit import *
from time import *
brightness= 0
brightness_control= 0
position_control= 0
x_position = 0
y_position = 0
while True:
    
    brightness_control = (display.read_light_level() // 10) * 10 
    brightness = display.read_light_level() - brightness_control 
    position_control = display.read_light_level() // 50
    y_position = 4 - position_control
    x_position = (display.read_light_level()-(position_control*50))// 10


    for i in range(5):
        if(i > y_position):
            for j in range(5):
                display.set_pixel(j,i,9)

        if(i < y_position):
            for j in range(5):
                display.set_pixel(j,i,0)
                
        if i == y_position:
            for j in range(5):
                if(j < x_position):
                    display.set_pixel(j,i,9)

                if(j > x_position):
                    display.set_pixel(j,i,0)
               
                


    if (y_position < 0):
        display.set_pixel(4,0, 9)
    else:
        display.set_pixel(x_position, y_position, brightness)
