# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:17:35 2017

@author: qinliu
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

SYN_file = 'tvb_abs_syn.npy'

func_conn_file = 'corr_syn_tvb.npy'

syn = np.load(SYN_file)

node_syn = []
node_ts = []
for i in range(998):
    node_syn.append(syn[:,0,1,0])
    node_ts.append(pd.Series(syn[:,0,1,0]))

mat_conn = np.zeros((998,998))
for x in range(998):
    for y in range(998):
        mat_conn[x][y] = node_ts[x].corr(node_ts[y],method='pearson')
        print x,y,mat_conn[x][y]
        
np.save(func_conn_file, mat_conn)


