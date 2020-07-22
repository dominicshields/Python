import turtle
import sys

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(0,0,100,100)
wn.tracer(100)
fred.up()

xave = 0
yave = 0
xtot = 0
ytot = 0
points = 0
infile = open("labdata.txt", "r")
aline = infile.readline()
while aline:
    points += 1
    items = aline.split()
#    print(items[0],items[1])
    xtot += int(items[0])
    ytot += int(items[1])
    fred.goto(int(items[0]),int(items[1]))
    fred.dot()          
    aline = infile.readline()
    
xave = xtot/points
yave = ytot/points
infile.close()

fred.down()
infile = open("labdata.txt", "r")
aline = infile.readline()
while aline:
    items = aline.split()
    x = int(items[0])
#    y = int(items[1])
    
    m = (xtot * ytot) - (points * xave * yave) / (xtot * xtot) - points * (xave * xave)
    y = yave + m * (x - xave)
    print("x =",x,"y =",y)
#    fred.goto(x,y)
    aline = infile.readline()

infile.close()

