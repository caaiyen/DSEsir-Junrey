from time import sleep 
from adafruit_circuitplayground import cp

num =  9
while True:
    if num == -1:
        num = 9
    if num == 10:
        num = 0
    cp.pixels[num] = 1
    print(num)
    sleep(0.5)
    cp.pixels[num] = 0

    if cp.switch:
        num +=1
    else:
        num -=1

















