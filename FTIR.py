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
import os
import platform
from matplotlib.widgets import Cursor


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


def find_file_names(file_path):
    for name in os.listdir (file_path):
        if name.endswith ('.dpt'):
            print (name)     
    file_names=[name for name in os.listdir(file_path) if name.endswith ('.dpt')]
    return file_names    
 
def switch_file_path():
    if platform.system() == 'Linux':
        file_path = '/home/kolan/mycode/python/forks/FTIR/data/'
        return file_path
    else:
        file_path = 'D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data\\'
        return file_path

def transtate_value_to_index(i, event_xdata):
    itemindex = np.where(x_list[i]<=event_xdata)
    return itemindex[0][0]
        
def onclick(event):
    global number_of_files
    plt.plot(event.xdata,event.ydata,'rs',ms=2,picker=5,label='cont_pnt')
    plt.axvline(x=event.xdata, visible=True)
    x_event.append(event.xdata)
    if x_event.__len__() == 2:
        for i in range (0, number_of_files):
            print trapz(y_list[i][transtate_value_to_index(i, x_event[0]):transtate_value_to_index(i, x_event[1])])
    plt.draw()
    
    
###############################################################################

file_path = switch_file_path()
file_names = find_file_names(file_path)

minima = []    
maxima = []
x_list = []
y_list = []
area = []

x_event = []

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, axisbg='#FFFFFF')

number_of_files = len(file_names)

for i in range (0, number_of_files):
    file_name = file_names[i]
    x, y = load_data(file_name, file_path)
    x_list.append(x)
    y_list.append(y)
    area=trapz(y)
    minima.append(y.min())
    maxima.append(y.max())
    y_norm = y / y.max()
    ax.plot (x, y_norm-y_norm.min()+1*i, label=str(i) + '. ' + file_name)
    print area

np_minima = np.asarray(minima)        # converts list to numpy array for .smin()
print 'Main minimum', np_minima.min()
ax.set_xlabel('Wavenumber [1/cm]')
ax.set_ylabel('Intentity [Arb. units]')
ax.set_title('All plots')
ax.invert_xaxis()
ax.grid()
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0-0.07, box.y0, box.width * 0.8, box.height])
# Put a legend to the right of the current axis
ax.legend(loc='left', bbox_to_anchor=(1, 1.012), prop={'size':12})

cursor = Cursor(ax, useblit=True, color='red', linewidth=2 )
cursor.horizOn = False
#pylab.savefig('All plots.png')
plt.gcf().canvas.mpl_connect('button_press_event',onclick)
#plt.legend(bbox_to_anchor=(1, 6),prop={'size':6})

plt.show()

    
    
    

    
   

