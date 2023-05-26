import board
from time import sleep
from digitalio import DigitalInOut, Direction

def main():
    ledGreen = DigitalInOut(board.D6)
    ledYellow = DigitalInOut(board.D7)
    ledRed = DigitalInOut(board.D8)

    ledGreen.direction = Direction.OUTPUT
    ledYellow.direction = Direction.OUTPUT
    ledRed.direction = Direction.OUTPUT

    while True:
        blinkeLED(ledGreen, .5)
        sleep(.5)
        blinkeLED(ledYellow, .5)
        sleep(.5)
        blinkeLED(ledRed, .5)
        sleep(.5)

def blinkeLED(led, delay):
    led.value = True
    sleep(delay)
    led.value = False

if __name__ == "__main__":
    main()