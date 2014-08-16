# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\klocek\.spyder2\.temp.py
"""
import numpy as np
from scipy. integrate import simps, trapz
import matplotlib.pyplot as plt
import pylab
from scipy.interpolate import splrep,splev
import sys
import os
from matplotlib.widgets import Cursor



event_x = []

def onclick(event):
    # when none of the toolbar buttons is activated and the user clicks in the
    # plot somewhere, compute the median value of the spectrum in a 10angstrom
    # window around the x-coordinate of the clicked point. The y coordinate
    # of the clicked point is not important. Make sure the continuum points
    # `feel` it when it gets clicked, set the `feel-radius` (picker) to 5 points
    toolbar = plt.get_current_fig_manager().toolbar
    if event.button==1 and toolbar.mode=='':
        window = ((event.xdata-5)<=x) & (x<=(event.xdata+5))
        #y2 = np.median(y[window])
        #y2 = np.asarray(y)     
        event_x.append(event.xdata)
        plt.plot(event.xdata,event.ydata,'rs',ms=10,picker=5,label='cont_pnt')
        print event.xdata
    plt.draw()


def onpick(event):
    # when the user clicks right on a continuum point, remove it
    if event.mouseevent.button==3:
        if hasattr(event.artist,'get_label') and event.artist.get_label()=='cont_pnt':
            event.artist.remove()
    ind=event.ind
    print ind
    print x
    print y
    



def ontype(event):
    # when the user hits enter:
    # 1. Cycle through the artists in the current axes. If it is a continuum
    #    point, remember its coordinates. If it is the fitted continuum from the
    #    previous step, remove it
    # 2. sort the continuum-point-array according to the x-values
    # 3. fit a spline and evaluate it in the wavelength points
    # 4. plot the continuum
    if event.key=='enter':
        cont_pnt_coord = []
        for artist in plt.gca().get_children():
            if hasattr(artist,'get_label') and artist.get_label()=='cont_pnt':
                cont_pnt_coord.append(artist.get_data())
            elif hasattr(artist,'get_label') and artist.get_label()=='continuum':
                artist.remove()
        cont_pnt_coord = np.array(cont_pnt_coord)[...,0]
        sort_array = np.argsort(cont_pnt_coord[:,0])
        x,y = cont_pnt_coord[sort_array].T
        spline = splrep(x,y,k=3)
        continuum = splev(x,spline)
        plt.plot(x,continuum,'r-',lw=2,label='continuum')

    # when the user hits 'n' and a spline-continuum is fitted, normalise the
    # spectrum
    elif event.key=='n':
        continuum = None
        for artist in plt.gca().get_children():
            if hasattr(artist,'get_label') and artist.get_label()=='continuum':
                continuum = artist.get_data()[1]
                break
        if continuum is not None:
            plt.cla()
            plt.plot(x,y/continuum,'k-',label='normalised')

    # when the user hits 'r': clear the axes and plot the original spectrum
    elif event.key=='r':
        plt.cla()
        plt.plot(x,y,'k-')

    # when the user hits 'w': if the normalised spectrum exists, write it to a
    # file.
    elif event.key=='w':
        for artist in plt.gca().get_children():
            if hasattr(artist,'get_label') and artist.get_label()=='normalised':
                data = np.array(artist.get_data())
                #np.savetxt(os.path.splitext(filename)[0]+'.nspec',data.T)
                print('Saved to file')
                break
    plt.draw()

def load_data(file_name, file_path):
   """
   Loads data from the EDX csv file
   :param file_name:
   :param file_path:
   :return: x_column, y_column raw data
   """

   file_name_and_path = file_path + file_name

   x_column, y_column = np.loadtxt(file_name_and_path, dtype=float, 
                                   delimiter=',', skiprows=0,
                                   usecols=(0, 1), unpack=True)
   return x_column, y_column

def file_name_without_extension(file_name):
   dot_position = file_name.find('.')
   return file_name[0:dot_position]

def image_name(file_name):
   return file_name_without_extension(file_name) + '.png'

###############################################################################


file_path = 'D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data\\'
for name in os.listdir (file_path):
    if name.endswith ('.dpt'):
        print (name)
        
a=[name for name in os.listdir('D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data') if name.endswith ('.dpt')]
file_name = a[0]
minima = []    
maxima = []
x_list = []
y_list = []

for i in range (0, len(a)):
    file_name = a[i]
    x, y = load_data(file_name, file_path)
    x_list.append(x)
    y_list.append(y)
    area=trapz(y)
    minima.append(y.min())
    maxima.append(y.max())
    y_norm = y / y.max()
    plt.figure('All plots')
    #plt.plot(x,y_norm)
    plt.plot (x, y_norm-y_norm.min()+1*i)
    print area

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, axisbg='#FFFFCC')
np_minima = np.asarray(minima)        # converts list to numpy array for .smin()
print 'Main minimum', np_minima.min()
plt.xlabel('Wavenumber [1/cm]')
plt.ylabel('Intentity [Arb. units]')
plt.title('All plots')
plt.gca().invert_xaxis()
plt.grid()
pylab.savefig('All plots.png')

 # Connect the different functions to the different events
plt.gcf().canvas.mpl_connect('key_press_event',ontype)
plt.gcf().canvas.mpl_connect('button_press_event',onclick)
plt.gcf().canvas.mpl_connect('pick_event',onpick) 

cursor = Cursor(ax, useblit=True, color='red', linewidth=2 )

plt.show()

    
    
    

    
   

