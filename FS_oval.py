#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:53:17 2022

@author: htesfaw18
"""

from scipy.io import loadmat
import numpy as np
# In[]

def calc_thetha(A, al, t):
    # A = 1 X 4, C = 4X1, al = 3,
    C = np.empty((4,t.size))
    C[0,:] = 1
    C[1,:] = np.cos(15*(t+al[0,0])*np.pi/180)
    C[2,:] = np.cos(15*(2*t+al[0,1])*np.pi/180)
    C[3,:] = np.cos(15*(3*t+al[0,2])*np.pi/180)
    return A@C
def calc_A(b, AL):
    # b is an 4 X 4 array
    AL = np.abs(AL)
    l = np.array([1, np.log10(AL), np.log10(AL)**2,  np.log10(AL)**3]).reshape(1,4)
    return l@b
#
def read_table(sfile, m):
    ds = loadmat(sfile)
    data = ds['starkov']
    inds = np.argwhere(np.isnan(data[:,0]))[:,0]
    i = 1+inds[m]
    if m ==2:
        j = data.shape[0]
    else:
        j = inds[m+1]
    bA = data[i:j,0:4]
    ba = data[i:j,4:]
    return(bA, ba)

#
def FS_oval(kp, mlt, m):
    sfile = r'data/starkov.mat'
    c0 = 18; c1 = -12.3; c2 =  27.2; c3 =  -2.0
    AL = c0+c1*kp+c2*kp**2+c3*kp**3
    bA, ba = read_table(sfile, m)
    A = calc_A(bA, AL)
    al =  calc_A(ba, AL)
    #
    thetha = calc_thetha(A, al, mlt)
    return thetha[0,:]