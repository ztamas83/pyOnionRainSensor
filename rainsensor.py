import gpio
import time

if __name__ == "__main__":
    try:
        while True:
            gpio.setup(0, gpio.IN)
            print(f'GPIO 0 state: {gpio.read(0)}')
            time.sleep(.5)
    except KeyboardInterrupt:
        pass
