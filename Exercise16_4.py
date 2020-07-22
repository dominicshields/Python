import math
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self,newp):
        dx = (newp.getX() - self.x)
        dy = (newp.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)

    def reflect_x(self,p):
        #return "y axis = " - p.y
        return "x=" + str(p.x) + ", y=" + str(- p.y)

    def slopeFromOrigin(self):
        px = self.x
        py = self.y
        return py/px

    def slope(self,target):
        if target.x == self.x:
            return None
        else:
            m = (target.y - self.y) / (target.x - self.x)
            return m

    def get_line_to(self,target):
        c = -(self.slope(target)*self.x - self.y)
        return 'y = ' + str(self.slope(target)) + 'x + ' + str(c)

def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point(4, 11)
print(p.get_line_to(Point(6, 15)))

