from microbit import *
from time import *
led = [
            [0,0],[1,0],[2,0],[3,0],[4,0],
            [4,1],[4,2],[4,3],[4,4],
            [3,4],[2,4],[1,4],[0,4],
            [0,3],[0,2],[0,1],
            [1,1],[2,1],[3,1],
            [3,2],[3,3],
            [2,3],[1,3],
            [1,2],[2,2]
            ]
while True:
    for i in range(0,len(led)):
        display.set_pixel(led[i][0], led[i][1], 9)
        sleep(0.5)
        display.set_pixel(led[i][0], led[i][1], 0)