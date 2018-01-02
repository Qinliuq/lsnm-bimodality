#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:57:19 2017

@author: qinliu
"""

import numpy as np
import matplotlib.pyplot as plt

endo = np.loadtxt('attna_b.out')
exo = np.loadtxt('attna_a.out')

mgns = np.loadtxt('mgns.out')
ead1 = np.loadtxt('ead1_c.out')
ead1_a = np.loadtxt('ead1_a.out')
ead1_b = np.loadtxt('ead1_b.out')
ead1_s = np.loadtxt('ead1_s.out')
ead2 = np.loadtxt('ead2_c.out')
ead2_a = np.loadtxt('ead2_a.out')
ead2_b = np.loadtxt('ead2_b.out')
ead2_s = np.loadtxt('ead2_s.out')
eafs = np.loadtxt('eafs.out')
eafs_a = np.loadtxt('eafs_a.out')
eafs_b = np.loadtxt('eafs_b.out')
eafs_s = np.loadtxt('eafs_s.out')
eafr = np.loadtxt('eafr.out')
eafr_a = np.loadtxt('eafr_a.out')
eafr_b = np.loadtxt('eafr_b.out')
eafr_s = np.loadtxt('eafr_s.out')
ea1d = np.loadtxt('ea1d.out')
ea1u = np.loadtxt('ea1u.out')
ea2d = np.loadtxt('ea2d.out')
ea2u = np.loadtxt('ea2u.out')
ea2c = np.loadtxt('ea2c.out')
estg = np.loadtxt('estg.out')
mtl = np.loadtxt('eaga_b.out')

a1 = ea1d + ea1u
m_a1 = np.mean(a1,axis=1)

a2 = ea2d + ea2u + ea2c
m_a2 = np.mean(a2,axis=1)

m_stg = np.mean(estg,axis=1)
m_mtl = np.mean(mtl,axis=1)
m_fs = np.mean(eafs_b,axis=1)
m_d1 = np.mean(ead1_b,axis=1)
m_d2 = np.mean(ead2_b,axis=1)

fr = [eafr_b[:,i] for i in [3,6,7,8,16,62,72,74,76]]
m_fr = np.mean(fr,axis = 0)

# Extract number of timesteps from one of the matrices
timesteps = mgns.shape[0]

print timesteps

# Contruct a numpy array of timesteps (data points provided in data file)
t = np.arange(0, timesteps, 1)

# Set up plot
plt.figure(1)

#plt.suptitle('Simulated mean neural activity')

ax = plt.subplot(9,1,1)
ax.plot(t,mgns)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('Input', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(9,1,2)
ax.plot(t,a1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('A1', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(9,1,3)
ax.plot(t,a2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('A2', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(9,1,4)
ax.plot(t,estg)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,0.9)
ax.set_xlim(0,timesteps)
plt.ylabel('ST', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(9,1,5)
ax.plot(t,mtl)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('MTL', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(9,1,6)
ax.plot(t,eafs_b)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('FS', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(9,1,7)
ax.plot(t,ead1_b)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('D1', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(9,1,8)
ax.plot(t,ead2_b)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('D2', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(9,1,9)
ax.plot(t,m_fr)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,0.4)
ax.set_xlim(0,timesteps)
plt.ylabel('R', rotation='horizontal', horizontalalignment='right')