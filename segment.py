#segment.py
# This program allows the user to draw a line segment and then displays
# the information textually and graphically

import math
from graphics import *

def main():
    win = GraphWin('Line segment info', 500, 500)
    win.setCoords(0,0,10,10)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    line = Line(p1,p2)
    line.setOutline('black')
    line.draw(win)

    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    slope = dy / dx
    length = math.sqrt(dx ** 2 + dy ** 2)
    midpoint = float(length/2)
    xmidc = float((p2.getX() + p1.getX())/2)
    ymidc = float((p2.getY() + p1.getY())/2)

    p3 = Circle(Point(xmidc,ymidc), 0.05)
    p3.setFill('cyan')
    p3.draw(win)

    print('first pair of points: ', Point(p1.getX(), p1.getY()))
    print('second pair of points: ', Point(p2.getX(), p2.getY()))
    print('line segment is: ', length)
    print('the midpoint of the line segment is ', midpoint)
    print('the midpoint coordinates are x = ', round((xmidc),2),
          "and y =", round(ymidc),2)
    print('the slope of the line segment is ', slope)

    win.getMouse()
    win.close()
main()


