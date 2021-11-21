# logic_board.py

from graphics import *
from button import Button

def draw_and(x,y,size,win):
        x1,x2 = x-size/2,x+size/2
        y1,y2 = y-size/2,y+size/2
        y3,y4 = y-size/4,y+size/4
        Line(Point(x1,y1),Point(x1,y2)).draw(win)
        Line(Point(x1,y1),Point(x2,y1)).draw(win)
        Line(Point(x1,y2),Point(x2,y2)).draw(win)
        Arc(Point(x,y1),Point(x+size,y2)).draw(win)
        # connectors
        Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
        Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
        Line(Point(x+size,y),Point(x+size+10,y)).draw(win)

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
    win = GraphWin('Logic Board',600,600)
    and_button = Button(win, Point(50,50), 60,40, "AND")
    and_button.activate()
    or_button = Button(win, Point(50,100), 60,40, "OR")
    or_button.activate()
    not_button = Button(win, Point(50,150), 60,40, "NOT")
    not_button.activate()
    xor_button = Button(win, Point(50, 200), 60, 40, "XOR")
    xor_button.activate()
    nand_button = Button(win, Point(50, 250), 60, 40, "NAND")
    nand_button.activate()
    while True:
        p = win.getMouse()
        if and_button.clicked(p):
                p1 = win.getMouse()
                draw_and(p1.getX(), p1.getY(), 60, win)
        elif or_button.clicked(p):
                p2 = win.getMouse()
                draw_or(p2.getX(), p2.getY(), 60, win)
        elif not_button.clicked(p):
                p3 = win.getMouse()
                draw_not(p3.getX(), p3.getY(), 60, win)
        elif xor_button.clicked(p):
                p4 = win.getMouse()
                draw_xor(p4.getX(), p4.getY(), 60, win)
        elif nand_button.clicked(p):
                p5 = win.getMouse()
                draw_nand(p5.getX(), p5.getY(), 60, win)
main()
