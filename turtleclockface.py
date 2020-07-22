import turtle
hours = 12
angle = 30
handlen = 140
dashlen = 7
gap = 20
centre = 0,0
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
alex.pensize(3)
alex.stamp()
alex.speed(8)
for x in range(hours):
    alex.penup()
    alex.forward(handlen)
    alex.pendown()
    alex.forward(dashlen)
    alex.penup()
    alex.forward(gap)
    alex.stamp()
    alex.goto(centre)
    alex.right(angle)
