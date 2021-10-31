# intersection.py
# This program computes the intersection of a circle with a horizontal line and
# displays the information textually and graphically
import math
from graphics import *

def main():
    radius = float(input("Enter the radius of the circle: "))
    y_int = float(input("Enter the y- intercept of the line: "))

    intersect = GraphWin("Circle and line", 100, 100)
    intersect.setCoords(-10.0,-10.0,10.0,10.0)
    c = Circle(Point(0.0,0.0), radius)
    mcircle = Circle(Point(0.0,0.0), 0.5)
    l = Line(Point(-10,y_int), Point(10,y_int))
    c.draw(intersect)
    mcircle.draw(intersect)
    l.draw(intersect)

    xint1 = 0
    xint2 = 0
    print("first x intercept: ", xint1)
    print("second x intercept: ", xint2)

    x = math.sqrt(radius ** 2 - y_int ** 2)
    yint1 = math.sqrt(radius ** 2- x ** 2)
    yint2 = -abs(yint1)
    print('first y root: ', yint1)
    print('second y root: ', yint2)

    spot1 = Circle(Point(x, yint1), 0.3)
    spot1.setFill('red')
    spot2 = Circle(Point(-x, yint1), 0.3)
    spot2.setFill('red')
    spot1.draw(intersect)
    spot2.draw(intersect)

    intersect.getMouse()
    
main()
