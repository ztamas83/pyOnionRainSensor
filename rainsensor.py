import gpio

if __name__ == "__main__":
    gpio.setup(0, gpio.IN)
    print(f'GPIO 0 state: {gpio.read(0)}')