# archery.py
# This program draws a target with its given colors necessary

from graphics import *

def main():
    archery = GraphWin("Archery Circle", 800, 800)
    c1 = Circle(Point(400, 400), 120)
    c2 = Circle(Point(400, 400), 100)
    c3 = Circle(Point(400, 400), 80)
    c4 = Circle(Point(400, 400), 60)
    c5 = Circle(Point(400, 400), 40)
    c1.draw(archery)
    c2.draw(archery)
    c3.draw(archery)
    c4.draw(archery)
    c5.draw(archery)
    c1.setFill('white')
    c2.setFill('black')
    c3.setFill('blue')
    c4.setFill('red')
    c5.setFill('yellow')
    
main()
