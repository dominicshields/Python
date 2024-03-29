import turtle
import sys

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'FF'   # Rule 1
    elif ch == 'X':
        newstr = '--FXF++FXF++FXF--'   # Rule 2
    else:
        newstr = ch              # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    sys.setExecutionLimit(40000)
    inst = createLSystem(5, "FXF--FF--FF")   # create the string
#    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.penup()  
    t.back(200)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    t.speed(0)
    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()



