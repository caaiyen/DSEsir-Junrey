from microbit import *
from time import sleep


while True:
    display.show(Image("90000:09000:00900:00090:00009"))
    sleep(0.5)
    display.show(Image("09000:00900:00090:00009:90000"))
    sleep(0.5)
    display.show(Image("00900:00090:00009:90000:09000"))
    sleep(0.5)
    display.show(Image("00900:00090:00009:90000:09000"))
    sleep(0.5)
    display.show(Image("00090:00009:90000:09000:00900"))
    sleep(0.5)
    display.show(Image("00009:90000:09000:00900:00090"))
    sleep(0.5)