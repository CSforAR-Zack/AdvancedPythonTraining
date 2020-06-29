from turtle import Turtle, Screen
def move(x):
    t.forward(x)

t = Turtle()
s = Screen()

s.listen()
z = 100
s.onkeypress(lambda : move(z), 'space')




#lambda : move(z)