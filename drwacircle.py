import turtle
def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)
def drawTriangle(t, sz):
    for i in range(3):
        t.forward(sz)
        t.left(120)
def drawOctagon(t, sz):
    for i in range(8):
        t.forward(sz)
        t.left(45)
def drawCircle(t, sz):
    for i in range(360):
        t.forward(sz)
        t.left(1)
def drawPolygon(t, sideLength, numSides):
    for i in range(numSides):
        t.forward(sideLength)
        t.left(360/numSides)
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(10)
drawSquare(alex, 50)
alex.penup()
alex.goto(-80,0)
alex.pendown()
drawTriangle(alex, 70)
alex.penup()
alex.goto(-80,100)
alex.pendown()
drawOctagon(alex, 30)
alex.penup()
alex.goto(-80,-130)
alex.pendown()
drawCircle(alex, 1)
alex.penup()
alex.goto(80,-130)
alex.pendown()
drawPolygon(alex,30,10)  # draw a decagon
