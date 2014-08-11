# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\klocek\.spyder2\.temp.py
"""
import numpy as np
import matplotlib.pyplot as plt
import pylab


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


import os
file_path = 'D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data\\'
for name in os.listdir (file_path):
    if name.endswith ('.dpt'):
        print (name)
        
a=[name for name in os.listdir('D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data') if name.endswith ('.dpt')]
file_name = a[0]
minima = []    
maxima = []

for i in range (0, len(a)):
    file_name = a[i]
    x, y = load_data(file_name, file_path)
    minima.append(y.min())
    maxima.append(y.max())
    y_norm = y / y.max()
    plt.figure('All plots')
    #plt.plot(x,y_norm)
    plt.plot (x, y_norm-y_norm.min()+1*i)

np_minima = np.asarray(minima)        # converts list to numpy array for .smin()
print 'Main minimum', np_minima.min()
plt.xlabel('Wavenumber [1/cm]')
plt.ylabel('Intentity [Arb. units]')
plt.title('All plots')
plt.gca().invert_xaxis()
plt.grid()
pylab.savefig('All plots.png')
plt.show()
    
   

