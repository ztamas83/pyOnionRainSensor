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
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("192.168.1.230", 1883, 60)

        client.loop_start()

        gpio.setup(0, gpio.IN)
        currentState = gpio.read(0)
        while True:
            newState = gpio.read(0)
            print(f'GPIO 0 state: {gpio.read(0)}')
            if (currentState != newState):
                infot = client.publish("rainsensor", newState)
                infot.wait_for_publish()
                currentState = newState
            time.sleep(.5)
    except KeyboardInterrupt:
        client.disconnect()
        pass
