#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:40:25 2022

@author: htesfaw18
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 18:28:39 2022

@author: htesfaw18
"""
from scipy.io import loadmat
import numpy as np
#
def calc_HP(kp):
    if kp<=5:
         HP = 38.66*np.exp(0.1967*kp)-33.99
    elif kp>5:
        HP = 4.592*np.exp(0.4731*kp)+20.47
    return HP
#
#
def oval_bound(mlt, kp, pelim, mlat, Q):
      cm = np.where(Q>=pelim, 1, 0) # comparison matrix
      ej = np.argmax(cm, 0)
      pj = np.argmax(np.flip(cm, 0), 0)
      eqlat = mlat[ej]
      pollat = np.flip(mlat)[pj]
      k1 = np.argwhere(ej == 0)[:,0]
      N = 0
      for i in k1:
          if np.all(cm[:,i])==0:
              eqlat[i] = np.NaN
              pollat[i] = np.NaN
              N = N+1
      return (eqlat, pollat)
#
def ZP_oval(mlt, kp, mlat, *arg, **kwargs):
    if arg:
        pelim = arg
    else:
        pelim = 0.25 
    zfile_new = r'data/zhang_new.mat'
    ds = loadmat(zfile_new)
    data = ds['zhang']
    #
    kpmodel = np.array([0.75, 2.25, 3.75, 5.25, 7.00, 9.00])
    angle = mlt*2*np.pi/24
    angle0 = angle.copy().reshape(mlt.size, 1)
    angle1 = np.tile(angle0, (1, 4))
    x = 90-mlat
    x0 = x.reshape(x.size, 1)
    x1 = np.tile(x0, (1, mlt.size))
    inds = np.argwhere(np.isnan(data[:,0]))[:,0]
    #
    Qmodel = np.zeros((6, mlat.size, mlt.size))
    for m in range(6):
        i = inds[m]+1    
        b0 = data[i,:]
        bc = data[i+1:i+7,:]
        bs = data[i+7:i+13,:]
        #
        S = np.zeros((mlt.size, 4))
        for n in range(6):
            k = n+1
            b1 = bc[n,:]
            b2 = bs[n,:]
            S = S+b1*np.cos(k*angle1)+b2*np.sin(k*angle1)
        #
        A = b0+S
        A0 = A[:, 0]
        A1 = A[:, 1]
        A2 = A[:, 2]
        A3 = A[:, 3]
        #
        Qmodel[m,:,:] = (A0*np.exp((x1-A1)/A2))/(1+np.exp((x1-A1)/A3))**2
    #
    kd = kpmodel-kp
    inds = np.where(kd<0, -1, 1)
    j = np.argwhere(kd>0)[0,0]
    if j==0:
        km = 0.75
        km1 = 2.25
        Qm = Qmodel[0,:,:]
        Qm1 = Qmodel[1,:,:]
    else:
        km = kpmodel[j-1]
        km1 = kpmodel[j]
        Qm = Qmodel[j-1,:,:]
        Qm1 = Qmodel[j,:,:]
    #
    HPm1 = calc_HP(km1)
    HPm = calc_HP(km)
    HP = calc_HP(kp)
    #
    fm = (HPm1-HP)/(HPm1-HPm)
    fm1 = (HP-HPm)/(HPm1-HPm)
    #
    Q = fm*Qm + fm1*Qm1
    (elat, plat) = oval_bound(mlt, kp, pelim, mlat, Q)
    return (Q, elat, plat)
