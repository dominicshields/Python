import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

wn = turtle.Screen()
poly = turtle.Turtle()
poly.color(input("What line colour?"))
poly.fillcolor(input("What fill colour?"))
poly.begin_fill()
drawPolygon(poly,int(input("How long do you want the sides?")),int(input("How many sides does the polygon have?")))
poly.end_fill()

wn.exitonclick()