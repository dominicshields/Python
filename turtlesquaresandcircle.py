import turtle

def drawspider(t,legs,len):
    for x in range(legs):
        t.left(360/legs)
        t.forward(len)
        t.left(rightangle)
        t.forward(100)
        t.forward(-200)
        t.right(rightangle)
        t.penup()
        t.goto(0,0)
        t.pendown()

rightangle = 90
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(1)
alex.speed(0)
drawspider(alex,20,100)