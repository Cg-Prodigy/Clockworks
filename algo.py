import pygame as py


class ClockWork:
    def __init__(self,x,y,rad,screen,color):
        self.x=x
        self.y=y
        self.rad=rad
        self.screen=screen
        self.color=color

    def theCircle(self):
        py.draw.circle(self.screen,self.color,(self.x,self.y), self.rad,2)
    def theLine(self,x2,y2):
        py.draw.line(self.screen, self.color,(self.x,self.y),(x2,y2), 2)


