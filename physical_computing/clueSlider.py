"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.
To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython
Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
import paho.mqtt.client as mqtt
import ast
topic = "clueSlider/#"
Sensors = {
    "clueSlider/temperature": [0],
    "clueSlider/acceleration": [0,0,0],
    "clueSlider/gyro": [0,0,0],
    "clueSlider/magnetic": [0,0,0],
    "clueSlider/pressure": [0],
    "clueSlider/altitude": [0],
    "clueSlider/humidity": [0],
    "clueSlider/proximity": [0],
    "clueSlider/color":[0,0,0,0]
}

# def updatelist(sensor):
#     Sensor[sensor].clear()
#     sensor.forEach(sensor=> sensor.push())
def display_text(sensor):
    print(tuple(sensor["clueSlider/gyro"]))
    clue_data[5].text = "Temperature: {} C".format(sensor["clueSlider/temperature"])
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(*tuple (sensor["clueSlider/acceleration"]))
    clue_data[1].text = "Gyro: {} {} {} dps".format(*tuple(sensor["clueSlider/gyro"]))
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*sensor["clueSlider/magnetic"])
    clue_data[3].text = "Pressure: {} hPa".format(sensor["clueSlider/pressure"])
    clue_data[4].text = "Altitude: {} m".format(sensor["clueSlider/altitude"])
    clue_data[6].text = "Humidity: {} %".format(sensor["clueSlider/humidity"])
    clue_data[7].text = "Proximity: {}".format(sensor["clueSlider/proximity"])
    clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(*sensor["clueSlider/color"])
    clue_data.show()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(topic)
        display_text(Sensors)

def on_message(client, userdata, msg):

    # display_text(msg.payload.decode())
    print(ast.literal_eval(msg.payload.decode()) )
    Sensors[msg.topic] = ast.literal_eval(msg.payload.decode())
    display_text(Sensors)
    

clue.sea_level_prqessure = 1020

clue_data = clue.simple_text_display(text_scale=2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()