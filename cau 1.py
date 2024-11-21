print("Nguyen Van Thai","\nMSSV: 235752021610005")
import turtle
wd=turtle.Screen()
wd.bgcolor("lightpink")
painter=turtle.Turtle()
painter.fillcolor('red')
painter.pencolor('purple')
painter.pensize(5)
def drawsq(t, s):
    for i  in range(4):
        t.forward(s)
        t.left(90)
for i in range(1,18):
    painter.left(22)
    drawsq(painter,200)
