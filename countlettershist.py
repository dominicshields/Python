import turtle

def countlet(text,dict):
    for c in text:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

def drawBar(t, data,offset):
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
        t.forward(11)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()                 # stop filling this shape           

dict = {}
countlet("Speaking to the Guardian ahead of International Women’s Day, Valeur criticised large listed companies for not achieving diversity targets. She said: “Do we really think that’s difficult? It’s a lie. It’s not difficult.",dict)

wn = turtle.Screen()
wn.setworldcoordinates(0,50,400,400)
arr = []
keylist = dict.keys()
keylist.sort()
for key in keylist:
    arr.append(dict[key])
    
#wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)
tess.speed(7)
drawBar(tess, arr, 5)