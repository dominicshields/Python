import turtle

def drawSquare(t, sz):
    for i in range(square):
        t.forward(sz)
        t.left(rightangle)
    movealex(t,shiftval)

def movealex(t,y):
    t.penup()
    t.right(shiftangle)
    t.forward(y)
    t.pendown()
    t.left(shiftangle)

rightangle = 90    
square = 4
squareinitlen = 20
shiftval = 15
shiftangle = 135

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("purple")
alex.pensize(2)
alex.speed(7)

x = squareinitlen 
for i in range(5):
    drawSquare(alex,x)
    x = x + squareinitlen
