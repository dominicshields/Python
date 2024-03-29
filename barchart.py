import turtle

def drawBar(t, data,offset):
     """ Get turtle t to draw one bar, of height. """
     for height in data:
         t.left(90)
         t.penup()
         t.forward(height+offset)
         t.write(str(height))     
         t.forward(-(height+offset))
         t.pendown()
         t.begin_fill()               # start filling this shape
         t.forward(height)
         t.right(90)
         t.forward(40)
         t.right(90)
         t.forward(height)
         t.left(90)
         t.end_fill()                 # stop filling this shape

xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10
legendoffset = 5

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)
tess.speed(7)

drawBar(tess, xs, legendoffset)

wn.exitonclick()
