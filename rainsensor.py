import gpio
import time
import paho.mqtt.client as mqtt

if __name__ == "__main__":
    try:
        gpio.setup(0, gpio.IN)
        while True:
            print(f'GPIO 0 state: {gpio.read(0)}')
            time.sleep(.5)
    except KeyboardInterrupt:
        pass
