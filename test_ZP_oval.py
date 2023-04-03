#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:36:06 2023

@author: htesfaw18
"""

import numpy as np
from ZP_oval import ZP_oval
#
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
# In[]
mlat = np.arange(30, 90, 0.5)
mlt = np.arange(0, 24, 0.01)
kp = 5
#
t, lat = np.meshgrid(mlt, mlat)
x = (np.pi/12)*t
y =  90 - lat
#
yticks = np.int32(np.arange(10, 90-50+1, 10))
yticklabel = 90-yticks
#
clim = 6
# In[]
#
fig, ax = plt.subplots(subplot_kw = {'projection':'polar'}, figsize = (6, 5))
plt.subplots_adjust(left=0.02, bottom=0.06,  right=0.89,  top=0.90)

(Q, elat, plat) = ZP_oval(mlt, kp, mlat, 0.25)
#
ax.grid(False) 
oval = ax.pcolormesh(x, y,  Q, cmap = 'nipy_spectral', vmin = 0, vmax = clim)
ax.plot(x[0, :], 90-elat, 'orangered')
ax.plot(x[0, :], 90-plat, 'orangered')

ax.set_ylim(0, 41)
ax.set_yticks(yticks)
#
xticks = ["%2.2i" % (xt*12/np.pi) for xt in ax.get_xticks()]
ax.xaxis.set_major_locator(mticker.FixedLocator(ax.get_xticks()))
ax.xaxis.set_major_formatter(mticker.FixedFormatter(xticks))
ax.set_theta_zero_location("S")
ax.set_xticklabels(xticks, fontsize = 13)
ax.set_yticks(yticks)
# ax.set_yticks(yticks, minor = True)
ax.set_yticklabels(yticklabel)
ax.set_rlabel_position(-160)
ax.grid(color = 'w', axis = 'y')
ax.tick_params(axis='y', colors='w')
ax.set_title("kp = "+str(kp), loc = 'right', fontsize = 13)
#
#
# # axins = inset_axes(ax, width = "60%",  height = "5%", borderpad = -5, loc = 'lower center')
# fig.colorbar(oval, ax = [axes[2], axes[5], axes[8]],  orientation="vertical", aspect = 50,
#           anchor = (2.5, 0.5), ticks = list(range(clim+1)), label = 'mWm$^{-2}$')
cb_ax = fig.add_axes([.86,.124,.02,.754])
cb = fig.colorbar(oval,orientation='vertical',cax=cb_ax)
cb.set_label(label = 'Auroral power [mWm$^{-2}$]', fontsize=13)
fig.show()
plt.savefig('figures/ZP_oval.png')