# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 09:19:58 2014

@author: klocek
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


file_path = 'D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data\\'

file_name = 'FTIR_ATR_After TGA 30-300C 10K-min_01.dpt'      

import os
for name in os.listdir ('D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data'):
    if name.endswith ('.dpt'):
        #'print (name)
        
a=[name for name in os.listdir(file_path) if name.endswith ('.dpt')]

x, y = load_data(file_name, file_path)

plt.figure(file_name_without_extension(file_name))
plt.gca().invert_xaxis()
plt.plot(x, y)
plt.title(file_name_without_extension(file_name))
plt.xlabel('Wavenumber [1/cm]')
plt.ylabel('Intentity [Arb. units]')
plt.grid()
pylab.savefig(image_name(file_name))
plt.show()
