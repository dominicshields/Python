import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
x = turtle.Turtle()
wn = turtle.Screen()
t.shape('turtle')
x.shape('turtle')
t.speed(0)
x.speed(0)
t.color("Blue")
x.color("Green")
t.penup()
x.penup()
t.goto(random.randrange(-100,100),random.randrange(-100,100))
x.goto(random.randrange(-100,100),random.randrange(-100,100))
t.pendown()
x.pendown()
while isInScreen(wn,t) and isInScreen(wn,x):
    t.left(random.randrange(0, 360))
    t.forward(random.randrange(1, 15))
    x.left(random.randrange(0, 360))
    x.forward(random.randrange(1, 15))

wn.exitonclick()


