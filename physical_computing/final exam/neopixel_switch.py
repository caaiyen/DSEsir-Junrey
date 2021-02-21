from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt
import ast
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        cp.red_led = True
        client.subscribe("cpxSwitch")
   

def on_message(client, userdata, msg):
    num =msg.payload.decode().split(",")
    
    if (num[1] == "true"):
        cp.pixels[int(num[0])] = (255, 255, 255)
    else: 
        cp.pixels[int(num[0])] = (0, 0, 0)

cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()