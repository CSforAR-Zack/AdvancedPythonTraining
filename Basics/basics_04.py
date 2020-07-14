from random import randint
from turtle import Turtle, Screen

def main():
    t = Turtle()
    s = Screen()
    t.speed(0)
    size = 1
    while True:
        t.forward(size)
        t.right(90)
        size += 2

    s.mainloop()


if __name__ == '__main__':
    main()