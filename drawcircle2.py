import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    anyTurtle.penup()
    anyTurtle.goto(0,radius)
    anyTurtle.pendown()
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

wn = turtle.Screen()
wheel = turtle.Turtle()
wheel.color("blue")
wheel.fillcolor("green")
wheel.begin_fill()
drawCircle(wheel, 90)
wheel.end_fill()

wn.exitonclick()