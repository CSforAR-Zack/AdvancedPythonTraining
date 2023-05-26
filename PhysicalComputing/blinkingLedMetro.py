import board
from time import sleep
from digitalio import DigitalInOut, Direction

def main():
    led = DigitalInOut(board.D7)
    led.direction = Direction.OUTPUT

    while True:
        led.value = True
        sleep(.5)
        led.value = False
        sleep(.5)
        
if __name__ == "__main__":
    main()