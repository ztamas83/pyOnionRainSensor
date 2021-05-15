import gpio
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

if __name__ == "__main__":
    try:
        gpio.setup(0, gpio.IN)
        
        while True:
            print(f'GPIO 0 state: {gpio.read(0)}')
            time.sleep(.5)
    except KeyboardInterrupt:
        pass
