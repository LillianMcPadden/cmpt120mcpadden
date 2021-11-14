# target.py
from graphics import *

class Target:

    def __init__(self, win, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin,self.ymin)
        p2 = Point(self.xmax,self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('red')
        self.rect.draw(win)
        self.label = Text(center,label)
        self.label.draw(win)

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    # You should have method that checks if the projectile hits the target
