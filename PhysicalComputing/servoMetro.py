import board
from time import sleep
import pwmio
from adafruit_motor import servo

def main():
    pwm = pwmio.PWMOut(board.A5, duty_cycle=2 ** 15, frequency=50)
    my_servo = servo.Servo(pwm)

    while True:
        for angle in range(0, 180, 5):
            my_servo.angle = angle
            sleep(.05)
        for angle in range(180, 0, -5):
            my_servo.angle = angle
            sleep(.05)

if __name__ == "__main__":
    main()