import pygame as py
from pygame.locals import *
from pygame.math import disable_swizzling
from algo import ClockWork
import random, math, time

py.init()

# global variables
s_tuple=(720,480)
caption='Clock works'
SCREEN=py.display.set_mode(s_tuple)
CAPTION=py.display.set_caption(caption)
FPS=py.time.Clock()
running=True
s_color=(36,36,36)
#  clock variables

x= s_tuple[0]/2
y=s_tuple[1]/2
color1= (0,255,255)
color2=(32,178,170)
rad=100

#  cirlce
t_clock= ClockWork(x,y,rad,SCREEN,color2)

#  second hand
s_hand= ClockWork(x,y,None,SCREEN,color1)
x2= x+rad/2 +15
y2=y+rad/2 +15

# time
t_seconds=time.localtime().tm_sec
if __name__=='__main__':
    while running:
        FPS.tick(24)
        SCREEN.fill(s_color)
        for event in py.event.get():
            if event.type==QUIT:
                running=False
        t_clock.theCircle()
        s_hand.theLine(x2,y2)
        py.display.update()
