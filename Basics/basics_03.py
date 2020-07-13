from random import randint
from turtle import Turtle, Screen

def main():
    t = Turtle()
    s = Screen()

    size = randint(100, 200)
    count = 0
    s.mainloop()

    while count < 4:
        t.forward(size)
        t.right(90)
        count += 1

    s.mainloop()


if __name__ == '__main__':
    main()