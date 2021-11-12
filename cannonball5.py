# cannonball5.py

from Projectile import Projectile
from tracker import Tracker
from target import Target
from graphics import *
from random import randrange

    
def getInputs():
    angle = float(input("Enter the launch angle(in degrees): "))
    vel = float(input("Enter the velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))
    win = GraphWin("Projectile", 200,200)
    tar = Target(win, Point(randrange(0,200),randrange(0,200)), 60, 40, "Target")
    cball = Projectile(angle, vel, h0)
    circle = Circle(Point(cball.getX(),cball.getY()),10)
    return angle, vel, h0, time, cball, circle, tar, win
    
def main():
    # get the input
    angle, vel, h0, time, cball, circle, tar, win = getInputs()
    track = Tracker(win, circle)

    # track the trajectory
    while cball.getY() >= 0:
        cball.update(time)
        if cball.getX() and cball.getY() == tar:
            break
        

    # output the distance
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))

main()
