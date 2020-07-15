from turtle import Turtle, Screen
from time import sleep

def main():
    t = Turtle()
    s = Screen()
    movement = 1
    direction = 1
    distance = 0
    
    t.hideturtle()
    s.tracer(0)
    t.left(90)

    while True:
        t.clear()
        t.forward(movement * direction)
        distance += movement
        t.dot(25, 'red')
        s.update()
        if distance > 200:
            direction = -direction
            distance = 0
        sleep(.01)

    s.mainloop()

if __name__ == '__main__':
    main()