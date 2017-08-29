# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:39:26 2017

@author: qinliu
"""

fileid = open('ea1uattna','w')
fileid.write('Connect(ea1u, attna) {'+'\n')
for i in range(80):
    fileid.write('From: (1,%d) { \n' % i)
    fileid.write('\t ([1,1] 0.025) \n  } \n')
fileid.write('}')