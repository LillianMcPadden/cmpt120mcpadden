# graphic_gates.py
# Program to draw logic gates

from graphics import *

# function to draw an AND gate
def draw_and(x,y,size,win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # outline
    Line(Point(x1,y1),Point(x1,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # connectors
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

# function to draw an OR gate
def draw_or(x,y,size,win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # Outline
    Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # Connectors
    Line(Point(x1,y3),Point(x-2,y3)).draw(win)
    Line(Point(x1,y4),Point(x-2,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

def draw_not(x,y,size,win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    #outline
    Line(Point(x1,y1),Point(x1,y2)).draw(win)
    Line(Point(x1,y1),Point(x+size,y)).draw(win)
    Line(Point(x1,y2),Point(x+size,y)).draw(win)
    #connector
    Line(Point(x1-10,y),Point(x1,y)).draw(win)
    Line(Point(x1-10,y),Point(x1,y)).draw(win)
    Circle(Point(x+size+6,y),5).draw(win)
    Line(Point(x+size+12,y),Point(x+size+24,y)).draw(win)

def draw_xor(x,y,size,win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # Outline
    Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # Connectors
    Arc(Point((x1-size/2)-8,y1),Point((x1+size/2)-8,y2)).draw(win)
    Line(Point(x1,y3),Point(x-2,y3)).draw(win)
    Line(Point(x1,y4),Point(x-2,y4)).draw(win)
    Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

def draw_nand(x,y,size,win):
    x1,x2 = x-size/2,x+size/2
    y1,y2 = y-size/2,y+size/2
    y3,y4 = y-size/4,y+size/4
    # outline
    Line(Point(x1,y1),Point(x1,y2)).draw(win)
    Line(Point(x1,y1),Point(x2,y1)).draw(win)
    Line(Point(x1,y2),Point(x2,y2)).draw(win)
    Arc(Point(x,y1),Point(x+size,y2)).draw(win)
    # connectors
    Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
    Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
    Circle(Point(x+size+6,y),5).draw(win)
    Line(Point(x+size+12,y),Point(x+size+24,y)).draw(win)

def main():
    win = GraphWin('Gate Graphics',600,600)
    draw_and(50,50,60,win)
    draw_or(50,150,60,win)
    draw_not(50,250,60,win)
    draw_xor(50,350,60,win)
    draw_nand(50,450,60,win)
    win.getMouse()
main()
