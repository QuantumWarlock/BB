# -*- coding: utf-8 -*-
"""
Created: Apr 2020
Classy Bouncing Balls!

@author: Ryan Clement (RRCC)
"""

import random
import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Ball Class
class Ball:
    """ Class for bouncing balls """
    ballCount = 0
    ay = -9.81             # m/s**2
    dt = 0.01              # s
    boxU = 10.0            # m
    boxD = 0.0             # m
    boxL = 0.0             # m
    boxR = 10.0            # m
    offset = 0.1

    def __init__(self, x=0, y=0, vx=0, vy=0):
        """ Constructor """
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.t = 0.0
        Ball.ballCount += 1

    def __del__(self):
        """ Destructor """
        Ball.ballCount -= 1

    def leapfrog(self):
        """ Leapfrog Integration Scheme for Gravity (2nd Order) """
        # Y
        self.y += self.vy*Ball.dt + Ball.ay*(Ball.dt*Ball.dt)/2.0
        self.vy += Ball.ay*Ball.dt
        if( self.y < Ball.boxD ):
            self.y = Ball.boxD + Ball.offset
            self.vy *= -1.0
        elif( self.y > Ball.boxU ):
            self.y = Ball.boxU - Ball.offset
            self.vy *= -1.0
        # X
        self.x += Ball.dt*self.vx
        if( self.x < Ball.boxL ):
            self.x = Ball.boxL + Ball.offset
            self.vx *= -1.0
        elif( self.x > Ball.boxR ):
            self.x = Ball.boxR - Ball.offset
            self.vx *= -1.0
        # Time
        self.t += Ball.dt

    def yoshida(self):
        """ Haruo Yoshida Integration Scheme for Gravity (4th Order) """
        cbrt2 = m.pow(2,1/3)
        w0 = cbrt2/(cbrt2 - 2.0)
        w1 = 1.0/(2.0 - cbrt2)
        c1 = w1/2.0
        c2 = (w0 + w1)/2.0
        y0 = self.y
        vy0 = self.vy
        y1 = y0 + c1*vy0*Ball.dt
        vy1 = vy0 + w1*Ball.ay*Ball.dt
        y2 = y1 + + c2*vy1*Ball.dt
        vy2 = vy1 + w0*Ball.ay*Ball.dt
        y3 = y2 + c2*vy2*Ball.dt
        vy3 = vy2 + w1*Ball.ay*Ball.dt
        self.y = y3 + c1*vy3*Ball.dt
        self.vy = vy3
        if( self.y < Ball.boxD ):
            self.y = Ball.boxD + Ball.offset
            self.vy *= -1.0
        elif( self.y > Ball.boxU ):
            self.y = Ball.boxU - Ball.offset
            self.vy *= -1.0
        # X
        self.x += Ball.dt*self.vx
        if( self.x < Ball.boxL ):
            self.x = Ball.boxL + Ball.offset
            self.vx *= -1.0
        elif( self.x > Ball.boxR ):
            self.x = Ball.boxR - Ball.offset
            self.vx *= -1.0
        # Time
        self.t += Ball.dt


# Animation Functions
def init():
    ap.set_data([],[])
    tText.set_text('Time = ')
    return ap, tText

def animate(i):
    s = 'Time = %.1f s' % ballList[0].t
    tText.set_text(s)
    xList = []
    yList = []
    for b in ballList:
        xList.append(b.x)
        yList.append(b.y)
        for i in np.arange(10):
            b.yoshida()
    ap.set_data(xList,yList)
    return ap,tText

# Movie Time!
fig, ax = plt.subplots()
ax.set_title('Bouncing Balls!')
ax.set_xlim([0,10])
ax.set_ylim([0,10])
tText = ax.text(4.5, 9.5, 'Time = ')
ap, = ax.plot([],[],'ro')

ballList = []
for i in range(100):
    xR  = random.uniform(4.9,5.1)
    yR  = random.uniform(4.9,5.1)
    vxR = random.uniform(-10.0,10.0)
    vyR = random.uniform(-10.0,10.0)
    ballList.append( Ball(xR,yR,vxR,vyR) )

ani = animation.FuncAnimation(fig, animate, frames=101,
                              interval=100, blit=True,
                              init_func=init, repeat=False)

# Uncomment next two lines to write file to disk.
#pwriter = animation.PillowWriter(fps=5, metadata=dict(artist='Dr. Ryan Clement'))
#ani.save('../movies/bouncing_balls.gif',writer=pwriter)

plt.show()
