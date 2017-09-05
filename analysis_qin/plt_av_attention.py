# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 10:48:39 2017

@author: qinliu
"""

import numpy as np
import matplotlib.pyplot as plt

lgns =np.loadtxt('lgns.out')
mgns = np.loadtxt('mgns.out')

attnv = np.loadtxt('attnv.out')
attna = np.loadtxt('attna_a.out')

timesteps = lgns.shape[0]
print timesteps

t = np.arange(0,timesteps)

plt.figure()
ax = plt.subplot(4,2,1)
ax.plot(t,lgns)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('visual stimuli saliency', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(4,2,3)
ax.plot(t,attnv)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1.5)
ax.set_xlim(0,timesteps)
plt.ylabel('visual attention', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(4,2,2)
ax.plot(t,mgns)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('auditory stimuli saliency', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(4,2,4)
ax.plot(t,attna)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('auditory attention', rotation='horizontal', horizontalalignment='right')

plt.show()
