#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:18:32 2017

@author: qinliu
"""

# ============================================================================
#
#                            PUBLIC DOMAIN NOTICE
#
#       National Institute on Deafness and Other Communication Disorders
#
# This software/database is a "United States Government Work" under the 
# terms of the United States Copyright Act. It was written as part of 
# the author's official duties as a United States Government employee and 
# thus cannot be copyrighted. This software/database is freely available 
# to the public for use. The NIDCD and the U.S. Government have not placed 
# any restriction on its use or reproduction. 
#
# Although all reasonable efforts have been taken to ensure the accuracy 
# and reliability of the software and data, the NIDCD and the U.S. Government 
# do not and cannot warrant the performance or results that may be obtained 
# by using this software or data. The NIDCD and the U.S. Government disclaim 
# all warranties, express or implied, including warranties of performance, 
# merchantability or fitness for any particular purpose.
#
# Please cite the author in any work or product based on this material.
# 
# ==========================================================================



# ***************************************************************************
#
#   Large-Scale Neural Modeling software (LSNM)
#
#   Section on Brain Imaging and Modeling
#   Voice, Speech and Language Branch
#   National Institute on Deafness and Other Communication Disorders
#   National Institutes of Health
#
#   This file (plot_neural_auditory.py) was created on March 25, 2015.
#
#
#   Author: Antonio Ulloa. Last updated by Antonio Ulloa on March 21, 2016  
# **************************************************************************/

# plot_neural_auditory.py
#
# Plot output data files of auditory delay-match-to-sample simulation

import numpy as np
import matplotlib.pyplot as plt

# Load data files
attnv = np.loadtxt('attnv.out')
attna = np.loadtxt('attna_a.out')
lgns = np.loadtxt('lgns.out')
evd1 = np.loadtxt('evd1.out')
evd1_a = np.loadtxt('evd1_a.out')
evd1_b = np.loadtxt('evd1_b.out')
evd1_s = np.loadtxt('evd1_s.out')
evd2 = np.loadtxt('evd2.out')
evd2_a = np.loadtxt('evd2_a.out')
evd2_b = np.loadtxt('evd2_b.out')
evd2_s = np.loadtxt('evd2_s.out')
evfs = np.loadtxt('evfs.out')
evfs_a = np.loadtxt('evfs_a.out')
evfs_b = np.loadtxt('evfs_b.out')
evfs_s = np.loadtxt('evfs_s.out')
evfr = np.loadtxt('evfr.out')
evfr_a = np.loadtxt('evfr_a.out')
evfr_b = np.loadtxt('evfr_b.out')
evfr_s = np.loadtxt('evfr_s.out')
ev1h = np.loadtxt('ev1h.out')
ev1v = np.loadtxt('ev1v.out')
ev4c = np.loadtxt('ev4c.out')
ev4h = np.loadtxt('ev4h.out')
ev4v = np.loadtxt('ev4v.out')
exss = np.loadtxt('exss.out')

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

# Extract number of timesteps from one of the matrices
timesteps = lgns.shape[0]

print timesteps

# Contruct a numpy array of timesteps (data points provided in data file)
t = np.arange(0, timesteps, 1)

# Set up plot
plt.figure(1)

plt.suptitle('SIMULATED NEURAL ACTIVITY')

# Plot lgn module
ax = plt.subplot(4,2,1)
ax.plot(t, lgns)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0.1,1)
ax.set_xlim(0,timesteps)
plt.ylabel('LGN', rotation='horizontal', horizontalalignment='right')


ax = plt.subplot(4,2,3)
ax.plot(t, evd1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('D1', rotation='horizontal', horizontalalignment='right')


ax = plt.subplot(4,2,5)
ax.plot(t, evd2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('D2', rotation='horizontal', horizontalalignment='right')

######################### AUDITORY #########################
# Plot MGN module
ax = plt.subplot(4,2,2)
ax.plot(t, mgns)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0.1,1)
ax.set_xlim(0,timesteps)
plt.ylabel('MGN', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(4,2,4)
ax.plot(t, ead1_s)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('D1', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(4,2,6)
ax.plot(t, ead2_s)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('D2', rotation='horizontal', horizontalalignment='right')

ax = plt.subplot(4,2,7)
ax.plot(t,attnv)
ax.set_yticks([])
ax.set_ylim(0,1)
ax.set_xlim(0,timesteps)
plt.ylabel('V attn',rotation='horizontal',horizontalalignment='right')

ax = plt.subplot(4,2,8)
ax.plot(t,attna)
ax.set_yticks([])
ax.set_ylim(0.3,0.9)
ax.set_xlim(0,timesteps)
plt.ylabel('A attn',rotation='horizontal',horizontalalignment='right')

# Show the plot on the screen
plt.show()

