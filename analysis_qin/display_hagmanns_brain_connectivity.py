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
#   This file (display_Hagmanns_brain_connectivity.py) was created on July 18, 2015.
#
#
#   Author: Antonio Ulloa. Last modified by Qin Liu on Dec. 15, 2016
#   Based on: display_sensor_locations.py by Paula Sanz-Leon (TVB team)
# **************************************************************************/

# display_Hagmanns_brain_connectivity.py
#
# Displays Hagmann's brain's 998-nodes plus LSNM nodes, along with the connections
# between Hagmann's nodes and LSNM nodes.

from tvb.simulator.lab import *
from tvb.simulator.plot.tools import mlab

# build an array of TVB nodes that you want to look at closely to visualize what is
# connected to what
# Below are the node numbers for the TVB nodes where visual LSNM modules are embedded
nodes_to_be_examined = [345, 393, 423, 418, 47, 74, 41, 125, 79, 474, 470, 477, 442, 48, 46, 78, 130, 80, 406]
#v1, v4, it, ec, fs, d1, d2, fr, attv, a1, a2, st, mtc, fs, d2, d1, fr, atta, perirhinal
# Below are the node numbers for the TVB nodes where auditory LSNM modules are embedded
#nodes_to_be_examined =[474, 470, 477,44]

# Define the hypothetical Talairach locations of each LSNM visual modules
v1_lsnm = [18,-88,8]
v4_lsnm = [30,-72,-12]
it_lsnm = [28,-36,-8]
ga_lsnm = [25,-12,-25]
vpf_lsnm = [42,26,20]

# define the hypothetical Talairach locations of each LSNM auditory module
#a1_lsnm = [48,-26,10]
#a2_lsnm = [62,-32,10]
#st_lsnm = [59,-17,4]
#apf_lsnm= [56,21,5]

# now, define the TVB nodes that are closest to the visual LSNM module locations above
v1 = [14, -86, 7]
v4 = [33, -70, -7]
it = [31, -39, -6]
ga = [25, -12, -25]
fs = [47, 19, 9]
d2 = [43, 29, 21]
d1 = [42, 39, 2]
fr = [29, 25, 40] 
att = [9, 57, 5]


# now, define the TVB nodes that are closest to the auditory LSNM module locations above
a1 = [51,-24,8]
a2 = [61,-36,12]
st = [59,-20,1]
mtc = [48, -58, 8]
fsa = [35, 19, 13]
d2a = [32, 29, 8]
d1a = [33, 31, 36]
fra = [33, 13, 28]
atta = [11, 64, 7]

#apf= [54,28,8]

pr = [37, -30, -19]

# Load connectivity from Hagmann's brain
white_matter = connectivity.Connectivity.from_file("connectivity_998.zip")
centres = white_matter.centres





# Plot the 998 nodes of Hagmann's brain
region_centres = mlab.points3d(centres[:, 0], 
                               centres[:, 1], 
                               centres[:, 2],
                               color=(0.5, 0.5, 0.5),
                               scale_factor = 1.)

# Now plot the hypothetical locations of LSNM visual modules

# V1 
v1_module = mlab.points3d(v1[0],v1[1],v1[2],color=(1, 1, 0),scale_factor = 5.)

# V4 
v4_module = mlab.points3d(v4[0],v4[1],v4[2],color=(1, 1, 0),scale_factor = 5.)

# IT 
it_module = mlab.points3d(it[0],it[1],it[2],color=(1, 1, 0),scale_factor = 5.)

ga_module = mlab.points3d(ga[0],ga[1],ga[2],color=(1,1,0),scale_factor = 5.)

# FS 
fs_module = mlab.points3d(fs[0],fs[1],fs[2],color=(1, 1, 0),scale_factor = 5.)

# D1
d1_module = mlab.points3d(d1[0],d1[1],d1[2],color=(1, 1, 0),scale_factor = 5.)

# D2
d2_module = mlab.points3d(d2[0],d2[1],d2[2],color=(1, 1, 0),scale_factor = 5.)

# FR 
fr_module = mlab.points3d(fr[0],fr[1],fr[2],color=(1, 1, 0),scale_factor = 5.)

# attention module
att_module = mlab.points3d(att[0],att[1],att[2],color=(1,1,0),scale_factor = 5.)

# ..., or plot the hypothetical locations of auditory LSNM modules
a1_module = mlab.points3d(a1[0],a1[1],a1[2],color=(0, 0, 1),scale_factor = 5.)
a2_module = mlab.points3d(a2[0],a2[1],a2[2],color=(0, 0, 1),scale_factor = 5.)
st_module = mlab.points3d(st[0],st[1],st[2],color=(0, 0, 1),scale_factor = 5.)
mtc_module = mlab.points3d(mtc[0],mtc[1],mtc[2],color=(0, 0, 1),scale_factor = 5.)
fsa_module = mlab.points3d(fsa[0],fsa[1],fsa[2],color=(0, 0, 1),scale_factor = 5.)
d1a_module = mlab.points3d(d1a[0],d1a[1],d1a[2],color=(0, 0, 1),scale_factor = 5.)
d2a_module = mlab.points3d(d2a[0],d2a[1],d2a[2],color=(0, 0, 1),scale_factor = 5.)
fra_module = mlab.points3d(fra[0],fra[1],fra[2],color=(0, 0, 1),scale_factor = 5.)
atta_module = mlab.points3d(atta[0],atta[1],atta[2],color=(0, 0, 1),scale_factor = 5.)

pr_module = mlab.points3d(pr[0],pr[1],pr[2],color=(1, 0, 0),scale_factor = 5.)
#apf_module = mlab.points3d(apf[0],apf[1],apf[2],color=(1, 0, 0),scale_factor = 8.)

print ' '

# ... now Plot the connections among the nodes
for tvb_node in nodes_to_be_examined:

    print 'Node ', tvb_node, ' is connected to nodes: [', 
    
    # extract TVB node numbers that are connected to TVB node above by a value larger than
    # a given threshold
    #tvb_conn = (white_matter.weights[tvb_node] > weight_threshold).nonzero()
    # get the connection that has the strongest weight
    tvb_conn = np.nonzero(white_matter.weights[tvb_node])
    # extract the numpy array from it
    tvb_conn = tvb_conn[0]
    
    for connected_node in tvb_conn:

        print connected_node, '(', white_matter.weights[tvb_node, connected_node], '),', 

        cxn = numpy.array([centres[connected_node],
                           centres[tvb_node]])

        connected = centres[connected_node]

        connections = mlab.plot3d(cxn[:, 0], cxn[:, 1], cxn[:, 2],
                                  color = (0, 0, 0),
                                  tube_radius=0.1)
        
        connected = mlab.points3d(connected[0], connected[1], connected[2],
                                color=(0.5, 0.5, 0.5),
                                scale_factor = 1.)

    print ']'

# Finally, show everything on screen
mlab.show(stop=True)
