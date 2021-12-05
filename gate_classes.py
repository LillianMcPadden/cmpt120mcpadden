#gate_classes.py

from graphics import *
from button import Button
class DigitalValue:

    def __init__(self,p,value):
        self.p = p
        self.value = value

    def getValue(self):
        return self.value
    
    def setValue(self,value):
        self.value.getValue(self.value)

    def draw(self,win,type):
        self.win = GraphWin('Logic classes',600,600)
        I = Entry(Point(self.p), 5)
        I2 = Entry(Point(self.p), 5)
        I.setText('')
        I2.setText('')
        O = Text(Point(500,500),'')
        button = Button(win, Point(400,400), 50, 50, 'run')
        button.draw(win)
        Rectangle(Point(100,100), Point(200,200)).draw(win)
        if type == 'I':
            I.draw(self.win)
            I2.draw(self.win)
        elif tpye == 'O':
            O.draw(win)
        else:
            print('Invalid type.')
        return self.win

class And:

    def __init__(self,p,a,b):
        self.p = p
        self.a = a
        self.b = b
        
    def setA(self,a):
        if self.a == 0:
            return 0
        else:
            return 1
        
    def setB(self,b):
        if self.b == 0:
            return 0
        else:
            return 1
        
    def getOutput(self):
        if self.a == 0 or self.b == 0:
            return 0
        else:
            return 1
        
    def draw(self,win):
        x1,x2 = 300-size/2,300+size/2
        y1,y2 = 300-size/2,300+size/2
        y3,y4 = 300-size/4,300+size/4
        # outline
        Line(Point(x1,y1),Point(x1,y2)).draw(win)
        Line(Point(x1,y1),Point(x2,y1)).draw(win)
        Line(Point(x1,y2),Point(x2,y2)).draw(win)
        Arc(Point(300,y1),Point(300+size,y2)).draw(win)
        # connectors
        Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
        Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
        Line(Point(300+size,300),Point(300+size+10,300)).draw(win)

class Or:

    def __init__(self,p,a,b):
        self.p = p
        self.a = a
        self.b = b
        
    def setA(self,a):
        if self.a == 0:
            return 0
        else:
            return 1
        
    def setB(self,b):
        if self.b == 0:
            return 0
        else:
            return 1
        
    def getOutput(self):
        if self.a == 1 or self.b == 1:
            return 1
        else:
            return 0
    
    def draw(self,win):
        x1,x2 = 300-size/2,300+size/2
        y1,y2 = 300-size/2,300+size/2
        y3,y4 = 300-size/4,300+size/4
        # Outline
        Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
        Line(Point(x1,y1),Point(x2,y1)).draw(win)
        Line(Point(x1,y2),Point(x2,y2)).draw(win)
        Arc(Point(300,y1),Point(300+size,y2)).draw(win)
        # Connectors
        Line(Point(x1,y3),Point(300-2,y3)).draw(win)
        Line(Point(x1,y4),Point(300-2,y4)).draw(win)
        Line(Point(300+size,300),Point(300+size+10,300)).draw(win)

class Not:

    def __init__(self,p,a,b):
        self.p = p
        self.a = a
        self.b = b
        
    def setA(self,a):
        if self.a == 0:
            return 0
        else:
            return 1
        
    def setB(self,b):
        if self.b == 0:
            return 0
        else:
            return 1
        
    def getOutput(self):
        if self.a == 1:
            return 0
        else:
            return 1
        
    def draw(self,win):
        x1,x2 = 300-size/2,300+size/2
        y1,y2 = 300-size/2,300+size/2
        #outline
        Line(Point(x1,y1),Point(x1,y2)).draw(win)
        Line(Point(x1,y1),Point(x+size,300)).draw(win)
        Line(Point(x1,y2),Point(x+size,300)).draw(win)
        #connector
        Line(Point(x1-10,300),Point(x1,300)).draw(win)
        Line(Point(x1-10,300),Point(x1,300)).draw(win)
        Circle(Point(300+size+6,300),5).draw(win)
        Line(Point(300+size+12,300),Point(300+size+24,300)).draw(win)

class Nand:

    def __init__(self,p,a,b):
        self.p = p
        self.a = a
        self.b = b
        
    def setA(self,a):
        if self.a == 0:
            return 0
        else:
            return 1
        
    def setB(self,b):
        if self.b == 0:
            return 0
        else:
            return 1
        
    def getOutput(self):
        if self.a == 0 or self.b == 0:
            return 1
        else:
            return 0
    
    def draw(self,win):
        x1,x2 = 300-size/2,300+size/2
        y1,y2 = 300-size/2,300+size/2
        y3,y4 = 300-size/4,300+size/4
        # outline
        Line(Point(x1,y1),Point(x1,y2)).draw(win)
        Line(Point(x1,y1),Point(x2,y1)).draw(win)
        Line(Point(x1,y2),Point(x2,y2)).draw(win)
        Arc(Point(300,y1),Point(300+size,y2)).draw(win)
        # connectors
        Line(Point(x1-10,y3),Point(x1,y3)).draw(win)
        Line(Point(x1-10,y4),Point(x1,y4)).draw(win)
        Circle(Point(300+size+6,300),5).draw(win)
        Line(Point(300+size+12,300),Point(300+size+24,300)).draw(win)        

class Xor:

    def __init__(self,p,a,b):
        self.p = p
        self.a = a
        self.b = b
        
    def setA(self,a):
        if self.a == 0:
            return 0
        else:
            return 1
        
    def setB(self,b):
        if self.b == 0:
            return 0
        else:
            return 1
        
    def getOutput(self):
        if (self.a == 0 and self.b == 0) or (self.a == 1 and self.b == 1):
            return 0
        else:
            return 1
    
    def draw(self,win):
        x1,x2 = 300-size/2,300+size/2
        y1,y2 = 300-size/2,300+size/2
        y3,y4 = 300-size/4,300+size/4
        # Outline
        Arc(Point(x1-size/2,y1),Point(x1+size/2,y2)).draw(win)
        Line(Point(x1,y1),Point(x2,y1)).draw(win)
        Line(Point(x1,y2),Point(x2,y2)).draw(win)
        Arc(Point(300,y1),Point(300+size,y2)).draw(win)
        # Connectors
        Arc(Point((x1-size/2)-8,y1),Point((x1+size/2)-8,y2)).draw(win)
        Line(Point(x1,y3),Point(300-2,y3)).draw(win)
        Line(Point(x1,y4),Point(300-2,y4)).draw(win)
        Line(Point(300+size,300),Point(300+size+10,300)).draw(win)

class Connection:

    def __init__(self, startFrom, goTo):
        self.startFrom = startFrom
        self.goTo = goTo
        
    def getFrom(self):
        return self.startFrom
    
    def getTo(self):
        return self.goTo
