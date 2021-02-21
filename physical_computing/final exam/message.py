from adafruit_clue import clue
import paho.mqtt.client as mqtt


clue_data = clue.simple_text_display( text_scale=2, title= "MESSAGE RECEIVER", title_color= clue.YELLOW)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("message")
        clue_data[0].text = "Connected"
        clue_data.show()

def on_message(client, userdata, msg):
    print(msg.payload.decode())

    clue_data[0].text = msg.payload.decode()
    clue_data.show()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()