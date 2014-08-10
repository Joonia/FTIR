# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 21:15:45 2014

@author: Jola
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

file_name = '1A_200X_5kV_01a.csv'      
file_path = 'C:\\Users\\Jola\\Desktop\\pd-dupa\\samples1_2_02072014\\EDX\\'
x_limit = 10

x, y = load_data(file_name, file_path)

plt.figure(file_name_without_extension(file_name))
plt.plot(x/100, y)
plt.title(file_name_without_extension(file_name))
plt.xlabel('Energy [keV]')
plt.ylabel('Intentity [Counts]')
pylab.xlim([0,x_limit])
pylab.savefig(image_name(file_name))
plt.show()