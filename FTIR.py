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

###############################################################################


file_path = switch_file_path()
file_names = find_file_names(file_path)

minima = []    
maxima = []

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, axisbg='#FFFFCC')

for i in range (0, len(file_names)):
    file_name = file_names[i]
    x, y = load_data(file_name, file_path)
    area=trapz(y)
    minima.append(y.min())
    maxima.append(y.max())
    y_norm = y / y.max()
    ax.plot (x, y_norm-y_norm.min()+1*i)
    print area

np_minima = np.asarray(minima)        # converts list to numpy array for .smin()
print 'Main minimum', np_minima.min()
ax.set_xlabel('Wavenumber [1/cm]')
ax.set_ylabel('Intentity [Arb. units]')
ax.set_title('All plots')
ax.invert_xaxis()
ax.grid()
cursor = Cursor(ax, useblit=True, color='red', linewidth=2 )
cursor.horizOn = False
pylab.savefig('All plots.png')
plt.show()

    
    
    

    
   

