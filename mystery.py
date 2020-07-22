import turtle
import sys

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-300,-300,400,300)
wn.tracer(100)


infile = open("mystery.txt", "r")
aline = infile.readline()
while aline:
    items = aline.split()
    if items[0] == "UP":
        fred.up()
    elif items[0] == "DOWN":
        fred.down()
    else:
        fred.goto(int(items[0]),int(items[1]))

    aline = infile.readline()

infile.close()