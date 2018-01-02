#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:50:19 2017

@author: qinliu
"""

import numpy as np
import matplotlib.pyplot as plt

fr = np.loadtxt('eafr_b.out')

timesteps = fr.shape[0]

print timesteps

# Contruct a numpy array of timesteps (data points provided in data file)
t = np.arange(0, timesteps, 1)

for i in range(fr.shape[1]):
    plt.figure(i)
    plt.plot(t, fr[:,i])
    