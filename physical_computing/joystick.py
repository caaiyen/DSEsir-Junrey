
from microbit import *
import paho.mqtt.client as mqtt

CIRCLE = Image("09990:90009:90009:90009:09990")
Direction = {
    "S": Image.ARROW_S,
    "SE": Image.ARROW_SE,
    "E": Image.ARROW_E,
    "NE":Image.ARROW_NE,
    "N": Image.ARROW_N,
    "NW": Image.ARROW_NW,
    "W": Image.ARROW_W,
    "SW": Image.ARROW_SW
}

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        display.show(Image.YES)
        client.subscribe("topic")

def on_message(client, userdata, msg):
    direction = msg.payload.decode()
    print(direction)
    if (direction in list (Direction.keys())):
        display.show(Direction [direction])
    else:
        display.show(Image("00000:00000:00000:00000:00000"))

    # print(msg.payload.decode())
    # if(msg.payload.decode() == "inside"):

    #     display.show(CIRCLE)
    # else:
    #     display.show(Image.NO)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()