# cannonball4.py

from Projectile import Projectile
from tracker import Tracker
from graphics import *

def getInputs():
    angle = float(input("Enter the launch angle(in degrees): "))
    vel = float(input("Enter the velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))
    return angle, vel, h0, time

def main():
    # get the input
    angle, vel, h0, time = getInputs()

    # create a projectile object
    cball = Projectile(angle, vel, h0)

    # create a window
    win = GraphWin("Projectile", 600,600)
    circle = Circle(Point(cball.getX(),cball.getY()),10)
    track = Tracker(win, circle)
    
    # track the trajectory
    while cball.getY() >= 0:
        cball.update(time)

    # output the distance
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))

    win.getMouse()

main()
