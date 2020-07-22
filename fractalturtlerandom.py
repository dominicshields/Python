import turtle
import random

def tree(branchLen,t,pensize):
    if branchLen > 5:
        t.pensize(pensize)
        t.forward(branchLen)
        randval = random.randrange(15, 45)
#        t.right(20)
        t.right(randval)
        tree(branchLen-15,t,pensize-1)
#        t.left(40)
        t.left(randval*2)
        tree(branchLen-15,t,pensize-1)
#        t.right(20)
        t.right(randval)
        t.backward(branchLen)

def main():
    pensize = 5
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("green")
    tree(75,t,pensize)
    myWin.exitonclick()

main()
