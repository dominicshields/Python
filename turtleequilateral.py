import turtle

def drawEquitriangle(t, sz):
    for i in range(3):
        t.left(120)
        t.forward(sz)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(1)
drawEquitriangle(alex, 150)