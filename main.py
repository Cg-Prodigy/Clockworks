# Cg-Prodigy
import pygame as py
import math
import time
import random
from pygame.locals import *
py.init()

# global variables
s_tuple = (720, 480)
caption = 'Clock works'
SCREEN = py.display.set_mode(s_tuple)
CAPTION = py.display.set_caption(caption)
FPS = py.time.Clock()
running = True
s_color = (36, 36, 36)
#  class


class Clockwork:
    def __init__(self, x, y, rad, color, screen):
        self.x = x
        self.y = y
        self.x2 = 0
        self.y2 = 0
        self.x3 = 0
        self.y3 = 0
        self.x4 = 0
        self.y4 = 0
        self.rad = rad
        self.color = color
        self.screen = screen
        self.omega = -math.pi/2

    def clock_circle(self):
        py.draw.circle(self.screen, self.color, (self.x, self.y), self.rad, 3)

    def sec_hand(self):
        py.draw.line(self.screen, self.color,
                     (self.x, self.y), (self.x2, self.y2), 1)
        seconds = (time.localtime().tm_sec/(math.pi*3))
        self.x2 = self.x + math.cos(self.omega+seconds)*self.rad
        self.y2 = self.y + math.sin(self.omega+seconds)*self.rad

    def minute_hand(self):
        py.draw.line(self.screen, self.color,
                     (self.x, self.y), (self.x3, self.y3), 2)
        minutes = time.localtime().tm_min/(math.pi*3)
        self.x3 = self.x + math.cos(self.omega+minutes)*(self.rad*3/4)
        self.y3 = self.y + math.sin(self.omega+minutes)*(self.rad*3/4)

    def hour_hand(self):
        py.draw.line(self.screen, self.color,
                     (self.x, self.y), (self.x4, self.y4), 3)
        hours = time.localtime().tm_hour
        self.x4 = self.x+math.cos(self.omega+hours)*(self.rad*1/2)
        self.y4 = self.y+math.sin(self.omega+hours)*(self.rad*1/2)
        return hours

#  utility functions


def randColor():
    r, g, b = random.randrange(0, 255), random.randrange(
        0, 255), random.randrange(0, 255)
    return r, g, b


#  clock variables
x = s_tuple[0]/2
y = s_tuple[1]/2
color2 = randColor()
rad = 150
t_clock = Clockwork(x, y, rad, color2, SCREEN)

#  seconds variable
color1 = randColor()
s_hand = Clockwork(x, y, rad, color1, SCREEN)

#  minute hand variables
color3 = randColor()
m_hand = Clockwork(x, y, rad, color3, SCREEN)
#  hour hand variables
color4 = randColor()
h_hand = Clockwork(x, y, rad, color4, SCREEN)
# main loop
while running:
    SCREEN.fill(s_color)
    for event in py.event.get():
        if event.type == QUIT:
            running = False
    t_clock.clock_circle()
    s_hand.sec_hand()
    m_hand.minute_hand()
    h_hand.hour_hand()
    py.display.update()
