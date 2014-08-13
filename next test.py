# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 09:19:58 2014

@author: klocek
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes



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

dtype = [('temp', 'f4'), ('depth', 'f4')]
kw = dict(usecols=(0, 1), dtype=dtype)
xbt_raw = np.genfromtxt("./data/C4_XBT_22.EDF", skiprows=41, **kw)
xbt_smoo = np.loadtxt('./data/C4_XBT_22.ASC', **kw)
ctd = np.loadtxt("./data/C4_CTD_22.ASC", **kw)

deg = u"\u00b0"
raw = dict(color='#FF8000', marker='.', linestyle='none', alpha=0.5, label='XBT Raw')
smoo = dict(color='#2E2E2E', linestyle='-.', label='XBT Smooth')
comp = dict(color='#0B610B', label='CTD')

fig, ax = plt.subplots(figsize=(4, 6))
ax.invert_yaxis()
ax.plot(ctd['depth'], ctd['temp'], **comp)
ax.plot(xbt_raw['depth'], xbt_raw['temp'], **raw)
ax.plot(xbt_smoo['depth'], xbt_smoo['temp'], **smoo)
ax.set_ylabel('Pressure [dbar]')
ax.set_xlabel(u'Temperature %sC' % deg)
ax.legend(numpoints=1, loc='upper left')

# Zoom 1.
axins = zoomed_inset_axes(ax, 5, loc=5)
axins.plot(ctd['depth'], ctd['temp'], **comp)
axins.plot(xbt_raw['depth'], xbt_raw['temp'], **raw)
axins.plot(xbt_smoo['depth'], xbt_smoo['temp'], **smoo)
axins.invert_yaxis()
axins.axis([3.5, 3.8, 1420, 1300])
axins.xaxis.tick_top()
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")
axins.xaxis.set_major_locator(MaxNLocator(nbins=1, prune='lower'))

# Zoom 2.
axins_2 = zoomed_inset_axes(axins, 10,  loc=4,
                     bbox_to_anchor=(1.2, 0.75),
                     bbox_transform=ax.figure.transFigure)

axins_2.plot(ctd['depth'], ctd['temp'], **comp)
axins_2.plot(xbt_raw['depth'], xbt_raw['temp'], **raw)
axins_2.plot(xbt_smoo['depth'], xbt_smoo['temp'], **smoo)
axins_2.axis([3.6, 3.75, 1360, 1340])
axins_2.invert_yaxis()
axins_2.set_yticks([])
axins_2.set_xticks([])
axins_2.set_axis_bgcolor('none')
axes = mark_inset(axins, axins_2, loc1=2, loc2=4, fc="none", ec="0.5")




