import turtle

def drawstar(t, sideLength,points):
    pointsangle = 360/points
    turnAngle = 180 - pointsangle/2
    for i in range(points):
        t.forward(sideLength)
        t.right(turnAngle)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
t = turtle.Turtle()
t.color("purple")
t.pensize(2)
t.speed(0)
t.penup()
t.goto(-100,0)
t.pendown()
drawstar(t, 200, 21)