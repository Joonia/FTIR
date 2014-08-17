# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 14:33:00 2014

@author: klocek
"""
import matplotlib.pyplot as plt
import pdb

class getBval:
    def __init__(self):
        figWH = (8,5) # in
        self.fig = plt.figure(figsize=figWH)
        plt.plot(range(10),range(10),'k--')
        self.ax = self.fig.get_axes()[0]
        self.x = [] # will contain 4 "x" values
        self.lines = [] # will contain 2D line objects for each of 4 lines            

        self.connect =    self.ax.figure.canvas.mpl_connect
        self.disconnect = self.ax.figure.canvas.mpl_disconnect

        self.mouseMoveCid = self.connect("motion_notify_event",self.updateCurrentLine)
        self.clickCid     = self.connect("button_press_event",self.onClick)
    def updateCurrentLine(self,event):
        xx = [event.xdata]*2
        self.currentLine, = self.ax.plot(xx,self.ax.get_ylim(),'k')
        plt.show()
    def onClick(self, event):
        if event.inaxes:
            self.updateCurrentLine(event)
            self.x.append(event.xdata)
            self.lines.append(self.currentLine)
            del self.currentLine
            if len(self.x)==4:
                self.cleanup()
    def cleanup(self):
        self.disconnect(self.mouseMoveCid)
        self.disconnect(self.clickCid)
        return self


xvals = getBval()
print xvals.x
 

    
 
    