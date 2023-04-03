#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:49:47 2023

@author: htesfaw18
"""

import numpy as np
from FS_oval import FS_oval
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
# In[]
smlt = np.arange(0, 24+0.15, 0.15)
x = (np.pi/12)*smlt
#
rlat = 66.73
rmlat = (90-rlat)*np.ones(x.size)
# 
yticks = np.arange(10, 41, 10)
yticklabel = 90-yticks
#
kp = 5
thetha0 = FS_oval(kp, smlt, 0) # poleward boundary of the main oval
thetha1 = FS_oval(kp, smlt, 1) # # equatorward boundary of the main oval
thetha2 = FS_oval(kp, smlt, 2) # # Equatorward boundary of the diffuse oval
#
#%%
fig, ax = plt.subplots(subplot_kw = {'projection':'polar'},figsize = (6, 6), \
                       gridspec_kw={'top':0.89, 'bottom':0.03, 'left':0.08, 'right':0.89});
ax.plot(x, thetha0, lw = 0)
ax.plot(x, rmlat, '--', color = 'magenta', lw = 1., zorder = 2, label = 'EISCAT radar')
ax.plot(x, thetha1, lw = 0)
ax.plot(x, thetha2,  color = 'yellow', lw =0.)
ax.fill_between(x, thetha0, thetha1, color = 'g', label = 'Main oval')
ax.fill_between(x, thetha1, thetha2, color = 'y', label='Diffuse oval')
#
ax.set_ylim(0, 40)
ax.set_yticks(yticks)
#
xticks = ["%2.2i" % (round(xt*12/np.pi)) for xt in ax.get_xticks()]
ax.xaxis.set_major_locator(mticker.FixedLocator(ax.get_xticks()))
ax.xaxis.set_major_formatter(mticker.FixedFormatter(xticks))
ax.set_xticklabels(xticks, fontsize=13)
ax.set_theta_zero_location("S")
ax.set_xticklabels(xticks, fontsize=13)
ax.set_yticklabels(yticklabel)
ax.grid(color = 'k', axis = 'y')
ax.grid(visible = False, axis = 'x')
ax.tick_params(axis='y', colors='k')
ax.text(0.9, 1.0, "Kp = "+str(kp),fontsize = 12, transform=ax.transAxes)
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc= (0.1, 0.95), fontsize = 12, ncol = 3)
plt.savefig('figures/FS_oval.png')
plt.show()