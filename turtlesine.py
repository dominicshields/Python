import math
import turtle

fred = turtle.Turtle()
sc = turtle.Screen()
sc.reset()
sc.setworldcoordinates(0,-1.5,360,1.5)

for angle in range(360):
    y = math.sin(math.radians(angle))
    fred.goto(angle,y) 
