import turtle
import math
import random

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
wn.tracer(100)
fred.up()
insideCount = 0
reps = 10000

for i in range(reps):
    randx = random.random()
    randy = random.random()
    randa = random.random()
    randb = random.random()

    if randa >= 0.5:
        x = randx
    else:
        x = -randx
    
    if randb >= 0.5:
        y = randy
    else:
        y = -randy
    
    fred.goto(x,y)
    if fred.distance(0,0) > 1:
        fred.color("Red")
    else:
        fred.color("Blue")
        insideCount += 1
        
    fred.dot()

print("Estimation of Pi =",(insideCount/reps)*4)
print("Reference value  = 3.1415926535897932384626433832795028")
wn.exitonclick()
