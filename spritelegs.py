import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(3)
alex.speed(0)
legs = input("How many legs does te spider have?")
for x in range(int(legs)):
    alex.left(360/int(legs))
    alex.forward(50)
    alex.goto(0,0)
   
