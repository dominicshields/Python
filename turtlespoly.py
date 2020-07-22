import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
donatello = turtle.Turtle()
donatello.color("purple")
donatello.pensize(2)

drawPolygon(donatello, 50, 8)