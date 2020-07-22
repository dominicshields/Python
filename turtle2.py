import turtle
moveval = 360
rightangle = 144
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(8)
alex.penup()
alex.goto(110,-160)
alex.pendown()
alex.right(-rightangle)
alex.forward(moveval)
for x in range(4):
    alex.right(rightangle)
    alex.forward(moveval)