class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


class Rectangle:
    """Rectangle class using Point, width and height"""

    def __init__(self, initP, initW, initH):

        self.location = initP
        self.width = initW
        self.height = initH
        
    def getwidth(self):
        return self.width

    def getheight(self):
        return self.height
    
    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)
    
    def transpose(self):
        holdw = self.width
        holdh = self.height
        self.width = holdh
        self.height = holdw
        return "width=" + str(self.width) + ", height=" + str(self.height)
    
    def __str__(self):    
        return "width=" + str(self.width) + ", height=" + str(self.height)

loc = Point(4, 5)
r = Rectangle(loc, 10, 5)
print(r)
print (r.getheight())
print (r.area())
print (r.perimeter())
print (r.transpose())
