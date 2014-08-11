# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 12:53:47 2014

@author: klocek
"""

file_path = 'D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data\\'

file_name = a[0]    

print file_name  

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

import os
for name in os.listdir ('D:\\ATS\\klocek\\Documents\\GitHub\\FTIR\\data'):
    if name.endswith ('.dpt'):
        'print (name)
        
a=[name for name in os.listdir(file_path) if name.endswith ('.dpt')]  

