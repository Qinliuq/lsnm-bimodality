# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 13:42:21 2017

@author: qinliu
"""
import numpy as np

import matplotlib.pyplot as plt
import scipy.stats as stats

BOLD_file = 'bold_balloon_TVB_ROI.npy'
SYN_file = 'synaptic_in_ROI.npy'
syn = np.load(SYN_file)
bold = np.load(BOLD_file)
#throw away the first value since it's always zero
v1_syn = np.delete(syn[0], 0)
v4_syn = np.delete(syn[1], 0)
it_syn = np.delete(syn[2], 0)
fs_syn = np.delete(syn[3], 0)
d1_syn = np.delete(syn[4], 0)
d2_syn = np.delete(syn[5], 0)
fr_syn = np.delete(syn[6], 0)
lit_syn = np.delete(syn[7], 0)
ec_syn = np.delete(syn[8], 0)
pfc_syn = np.delete(syn[9], 0)

v1_syn = (v1_syn-v1_syn.min()) / (v1_syn.max() - v1_syn.min())
v4_syn = (v4_syn-v4_syn.min()) / (v4_syn.max() - v4_syn.min())
it_syn = (it_syn-it_syn.min()) / (it_syn.max() - it_syn.min())
fs_syn = (fs_syn-fs_syn.min()) / (fs_syn.max() - fs_syn.min())
d1_syn = (d1_syn-d1_syn.min()) / (d1_syn.max() - d1_syn.min())
d2_syn = (d2_syn-d2_syn.min()) / (d2_syn.max() - d2_syn.min())
fr_syn = (fr_syn-fr_syn.min()) / (fr_syn.max() - fr_syn.min())
lit_syn= (lit_syn-lit_syn.min()) / (lit_syn.max() - lit_syn.min())
ec_syn = (ec_syn-ec_syn.min())/(ec_syn.max() - ec_syn.min())
pfc_syn = (pfc_syn-pfc_syn.min())/(pfc_syn.max() - pfc_syn.min())

v1_BOLD = np.delete(bold[0],0)
v4_BOLD = np.delete(bold[1],0)
it_BOLD = np.delete(bold[2],0)
fs_BOLD = np.delete(bold[3],0)
d1_BOLD = np.delete(bold[4],0)
d2_BOLD = np.delete(bold[5],0)
ec_BOLD = np.delete(bold[8],0)
pfc_BOLD= np.delete(bold[9],0)

mDMS_v1_syn = np.mean(v1_syn[20:500])
mDMS_v4_syn = np.mean(v4_syn[20:500])
mDMS_it_syn = np.mean(it_syn[20:500])
mDMS_ec_syn = np.mean(ec_syn[20:500])
mDMS_pfc_syn = np.mean(pfc_syn[20:500])

print 'the mean DMS of v1 v4 it ec pfc are ', mDMS_v1_syn, mDMS_v4_syn, mDMS_it_syn, mDMS_ec_syn, mDMS_pfc_syn

sDMS_v1_syn = np.std(v1_syn[20:500])
sDMS_v4_syn = np.std(v4_syn[20:500])
sDMS_it_syn = np.std(it_syn[20:500])
sDMS_ec_syn = np.std(ec_syn[20:500])
sDMS_pfc_syn = np.std(pfc_syn[20:500])
print 'the sd DMS are ', sDMS_v1_syn,sDMS_v4_syn,sDMS_it_syn,sDMS_ec_syn,sDMS_pfc_syn

mDMS_v1_synctrl = np.mean(v1_syn[1000:2360])
mDMS_v4_synctrl = np.mean(v4_syn[1000:2360])
mDMS_it_synctrl = np.mean(it_syn[1000:2360])
mDMS_ec_synctrl = np.mean(ec_syn[1000:2360])
mDMS_pfc_synctrl = np.mean(pfc_syn[1000:2360])
print 'the mean DMS ctrl are', mDMS_v1_synctrl,mDMS_v4_synctrl,mDMS_it_synctrl,mDMS_ec_synctrl,mDMS_pfc_synctrl

sDMS_v1_synctrl = np.std(v1_syn[1000:2360])
sDMS_v4_synctrl = np.std(v4_syn[1000:2360])
sDMS_it_synctrl = np.std(it_syn[1000:2360])
sDMS_ec_synctrl = np.std(ec_syn[1000:2360])
sDMS_pfc_synctrl = np.std(pfc_syn[1000:2360])
print 'sd DMS ctrl ',sDMS_v1_synctrl,sDMS_v4_synctrl,sDMS_it_synctrl,sDMS_ec_synctrl,sDMS_pfc_synctrl

v1_syn_DMS_change = (mDMS_v1_syn - mDMS_v1_synctrl)/mDMS_v1_synctrl
v4_syn_DMS_change = (mDMS_v4_syn - mDMS_v4_synctrl)/mDMS_v4_synctrl
it_syn_DMS_change = (mDMS_it_syn - mDMS_it_synctrl)/mDMS_it_synctrl
ec_syn_DMS_change = (mDMS_ec_syn - mDMS_ec_synctrl)/mDMS_ec_synctrl
pfc_syn_DMS_change = (mDMS_pfc_syn - mDMS_pfc_synctrl)/mDMS_pfc_synctrl

t_DMS_v1 = stats.ttest_rel(v1_syn[20:500],v1_syn[1000:1300])
t_DMS_v4 = stats.ttest_rel(v4_syn[20:500],v4_syn[1000:1300])
t_DMS_it = stats.ttest_rel(it_syn[20:500],it_syn[1000:1300])
t_DMS_ec = stats.ttest_rel(ec_syn[20:500],ec_syn[1000:1300])
t_DMS_pfc = stats.ttest_rel(pfc_syn[20:500],pfc_syn[1000:1300])
print 'ttest DMS ', t_DMS_v1, t_DMS_v4, t_DMS_it, t_DMS_ec, t_DMS_pfc



