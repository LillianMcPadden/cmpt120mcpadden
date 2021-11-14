# tracker.py
from graphics import *

class Tracker:

    def __init__(self, window, objToTrack):
        # window is a graphWin and objToTrack is an object whose
        # position is to be shows in the window. objToTrack must be
        # an object that has getX() and getY() methods that report its
        # current position
        # creates a tracker object and draws a circle in window
        # at the current position of objToTrack
        self.objToTrack = objToTrack
        self.circ = objToTrack # This is not a graphical object
        self.circ.draw(window)
        self.x = 0.0
        self.y = 0.0

    def update(self):
        # moves the circle in the window to the current position of the
        # object being tracked
        point = self.circ.getCenter()
        x = point.getX()
        y = point.getY()
        self.circ.move(self.objToTrack.getX() - x, self.objToTrack.getY()-y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y
