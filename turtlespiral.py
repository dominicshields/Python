import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(1)
alex.speed(0)

alexlen = 1 
for i in range(100):
    alex.right(89)
    alex.forward(alexlen)
    alexlen = alexlen + 2
