from microbit import * 
from time import sleep 
index = 0 
while True: 
    index = 0  if index > 28 else index
    led = "00000:00000:00000:00000:00000" 
    led_list = list(led) 
    total = len(led_list) 
    for i in range(0, total): 
        if led_list[i] == ':': 
            continue 
        if i == index:
            led_list[i] = '9' 
        else: 
            led_list[i] = '0' 
    index = index + 1 
    led = "".join(led_list) 
    display.show(Image(led)) 
    sleep(0.5)