from turtle import Turtle, Screen
from random import randint

def main():
    t = Turtle()
    s = Screen()
    # s.tracer(0)
    s.bgcolor('black')
    t.color('cyan')
    t.speed(0)
    t.penup()
    t.hideturtle()

    colors = ['hotpink', 'orange', 'cyan']

    for dot in range(500):
        x = randint(-500,500)
        y = randint(-500,500)
        t.goto(x,y)
        size = randint(10, 75)

        if x > 200:
            color = colors[2]
        elif x < -200:
            color = colors[0]
        else:
            color = colors[1]

        t.dot(size,color)
    # s.update()
    s.mainloop()

if __name__ == '__main__':
    main()