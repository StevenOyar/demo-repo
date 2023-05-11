from turtle import *


tik = Turtle()
screen = Screen()
tik.speed("fastest")
screen.title("Color POlygon ")
tik.hideturtle()

colors = ['red', 'purple', 'blue', 'green', 'orange', 'grey', 'teal', 'brown', 'white', 'cyan', 'indigo', 'yellow']

tik.pen()
screen.bgcolor('black')
for x in range(360):
    tik.pencolor(colors[x % 12])
    tik.width(x // 60 + 1)
    tik.forward(x)
    tik.left(59)



screen.mainloop()
