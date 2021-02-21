from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        cp.red_led = True
        client.subscribe("cpxSwitch0")
    elif rc == 1:
        cp.red_led = True
        client.subscribe("cpxSwitch1")
    elif rc == 2:
        cp.red_led = True
        client.subscribe("cpxSwitch2")

def on_message(client, userdata, msg):
    if msg.payload.decode() == "true":
        cp.pixels[0] = (255, 255, 255)
    else:
        cp.pixels[0] = (0, 0, 0)

cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt