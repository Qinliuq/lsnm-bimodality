#!/usr/bin/python
#
# The following script implements visual-auditory bimodal DMS trials with both endogenours and exogenous attention.
#
# There are 6 trials in each modality running simutaneously: 3 DMS trials and 3 control trials.
#
# The endogenous attention is set to attend visual stimuli, the exogenous attention is coupled with the saliency of inputs.
#
# The DMS trials are MATCH, MATCH, MATCH. The attention parameter in DMS trials is 0.3
# The control trials are 'passive viewing': random shapes are presented and low attention (0.05)
# is used. Passive viewing trials are also organized as MATCH, MISMATCH, MATCH.
#
# The first 240 timesteps = 1200 ms we do nothing. We assume 1 timestep = 5 ms, as in Horwitz
# et al (2005)
#


#!/usr/bin/python
#
# The following script is a test of the AV associated model.
#
# A list of stimuli (A/V) are shown.
#
# Total number of timesteps is 5400. (200 time steps = 1 second)
#
LSNM_simulation_time = 4500

# Define list of parameters the script is going to need to modify the LSNM neural network
# They are organized in the following order:
# [lo_att_level, hi_att_level, lo_inp_level, hi_inp_level, att_step, ri1, ri2]

script_params = [0.0, 0.3, 0.05, 0.5, 0.7, 0.9, 0.1]

def delay_period(modules, script_params):
    
    """
        modifies neural network with delay period parameters given
        
        """
    
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['lgns'][0]):
        for y in range(modules['lgns'][1]):
            modules['lgns'][8][x][y][0] = script_params[2]
    modules['attnv'][8][0][0][0] = script_params[6]
    modules['attnv_re'][8][0][0][0] = script_params[2]
    modules['attnv_a'][8][0][0][0] = script_params[2]
    modules['attnv_b'][8][0][0][0] = script_params[2]
    modules['attnv_s'][8][0][0][0] = script_params[2]
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['mgns'][0]):
        for y in range(modules['mgns'][1]):
            modules['mgns'][8][x][y][0] = script_params[2]
    modules['attna_re'][8][0][0][0] = script_params[2]
    modules['attna_c'][8][0][0][0] = script_params[2]
    modules['attna_a'][8][0][0][0] = script_params[6]
    modules['attna_b'][8][0][0][0] = script_params[2]
    modules['attna_s'][8][0][0][0] = script_params[2]

def intertrial_interval(modules, script_params):
    """
        resets the visual inputs and short-term memory using given parameters
        
        """
    
    # reset D1
    for x in range(modules['evd1'][0]):
        for y in range(modules['evd1'][1]):
            modules['evd1'][8][x][y][0] = script_params[0]
    # reset D2
    for x in range(modules['evd2'][0]):
        for y in range(modules['evd2'][1]):
            modules['evd2'][8][x][y][0] = script_params[0]

# reset D1
for x in range(modules['evd1_a'][0]):
    for y in range(modules['evd1_a'][1]):
        modules['evd1_a'][8][x][y][0] = script_params[0]
    # reset D2
    for x in range(modules['evd2_a'][0]):
        for y in range(modules['evd2_a'][1]):
            modules['evd2_a'][8][x][y][0] = script_params[0]

# reset D1
for x in range(modules['evd1_b'][0]):
    for y in range(modules['evd1_b'][1]):
        modules['evd1_b'][8][x][y][0] = script_params[0]
    # reset D2
    for x in range(modules['evd2_b'][0]):
        for y in range(modules['evd2_b'][1]):
            modules['evd2_b'][8][x][y][0] = script_params[0]

# reset D1
for x in range(modules['evd1_s'][0]):
    for y in range(modules['evd1_s'][1]):
        modules['evd1_s'][8][x][y][0] = script_params[0]
    # reset D2
    for x in range(modules['evd2_s'][0]):
        for y in range(modules['evd2_s'][1]):
            modules['evd2_s'][8][x][y][0] = script_params[0]
    
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['lgns'][0]):
        for y in range(modules['lgns'][1]):
            modules['lgns'][8][x][y][0] = script_params[2]
# reset D1
for x in range(modules['ead1_c'][0]):
    for y in range(modules['ead1_c'][1]):
        modules['ead1_c'][8][x][y][0] = script_params[0]
    # reset D2
    for x in range(modules['ead2_c'][0]):
        for y in range(modules['ead2_c'][1]):
            modules['ead2_c'][8][x][y][0] = script_params[0]

# reset D1
for x in range(modules['ead1_a'][0]):
    for y in range(modules['ead1_a'][1]):
        modules['ead1_a'][8][x][y][0] = script_params[0]
    # reset D2
    for x in range(modules['ead2_a'][0]):
        for y in range(modules['ead2_a'][1]):
            modules['ead2_a'][8][x][y][0] = script_params[0]

# reset D1
for x in range(modules['ead1_b'][0]):
    for y in range(modules['ead1_b'][1]):
        modules['ead1_b'][8][x][y][0] = 0.
    # reset D2
    for x in range(modules['ead2_b'][0]):
        for y in range(modules['ead2_b'][1]):
            modules['ead2_b'][8][x][y][0] = 0.

# reset D1
for x in range(modules['ead1_s'][0]):
    for y in range(modules['ead1_s'][1]):
        modules['ead1_s'][8][x][y][0] = 0.
    # reset D2
    for x in range(modules['ead2_s'][0]):
        for y in range(modules['ead2_s'][1]):
            modules['ead2_s'][8][x][y][0] = 0.

for x in range(modules['ea1d'][0]):
    for y in range(modules['ea1d'][1]):
        modules['ea1d'][8][x][y][0] = 0.
    
    for x in range(modules['ea1u'][0]):
        for y in range(modules['ea1u'][1]):
            modules['ea1u'][8][x][y][0] = 0.

for x in range(modules['ea2u'][0]):
    for y in range(modules['ea2u'][1]):
        modules['ea2u'][8][x][y][0] = 0.
    
    for x in range(modules['ea2d'][0]):
        for y in range(modules['ea2d'][1]):
            modules['ea2d'][8][x][y][0] = 0.

for x in range(modules['ea2c'][0]):
    for y in range(modules['ea2c'][1]):
        modules['ea2c'][8][x][y][0] = 0.
    
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['mgns'][0]):
        for y in range(modules['mgns'][1]):
            modules['mgns'][8][x][y][0] = script_params[0]
    # turn attention to 'LO', as the current trial has ended
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    modules['attnv'][8][0][0][0] = script_params[0]
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attna_re'][8][0][0][0] = script_params[0]
    modules['attna_a'][8][0][0][0] = script_params[0]
    modules['attna_b'][8][0][0][0] = script_params[0]
    modules['attna_s'][8][0][0][0] = script_params[0]
    modules['attna_c'][8][0][0][0] = script_params[0]

def firstStimulusUshape(modules, script_params):
    
    """
        generates a u-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[1]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][2][1][0] = script_params[3]
    modules['lgns'][8][3][1][0] = script_params[3]
    modules['lgns'][8][4][1][0] = script_params[3]
    modules['lgns'][8][5][1][0] = script_params[3]
    modules['lgns'][8][6][1][0] = script_params[3]
    modules['lgns'][8][7][1][0] = script_params[3]
    modules['lgns'][8][7][2][0] = script_params[3]
    modules['lgns'][8][7][3][0] = script_params[3]
    modules['lgns'][8][7][4][0] = script_params[3]
    modules['lgns'][8][7][5][0] = script_params[3]
    modules['lgns'][8][7][6][0] = script_params[3]
    modules['lgns'][8][2][7][0] = script_params[3]
    modules['lgns'][8][3][7][0] = script_params[3]
    modules['lgns'][8][4][7][0] = script_params[3]
    modules['lgns'][8][5][7][0] = script_params[3]
    modules['lgns'][8][6][7][0] = script_params[3]
    modules['lgns'][8][7][7][0] = script_params[3]

def secondStimulusUshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[1]
    
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][2][1][0] = script_params[3]
    modules['lgns'][8][3][1][0] = script_params[3]
    modules['lgns'][8][4][1][0] = script_params[3]
    modules['lgns'][8][5][1][0] = script_params[3]
    modules['lgns'][8][6][1][0] = script_params[3]
    modules['lgns'][8][7][1][0] = script_params[3]
    modules['lgns'][8][7][2][0] = script_params[3]
    modules['lgns'][8][7][3][0] = script_params[3]
    modules['lgns'][8][7][4][0] = script_params[3]
    modules['lgns'][8][7][5][0] = script_params[3]
    modules['lgns'][8][7][6][0] = script_params[3]
    modules['lgns'][8][2][7][0] = script_params[3]
    modules['lgns'][8][3][7][0] = script_params[3]
    modules['lgns'][8][4][7][0] = script_params[3]
    modules['lgns'][8][5][7][0] = script_params[3]
    modules['lgns'][8][6][7][0] = script_params[3]
    modules['lgns'][8][7][7][0] = script_params[3]

def thirdStimulusNshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[1]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'n' shape
    modules['lgns'][8][2][1][0] = script_params[5]
    modules['lgns'][8][3][1][0] = script_params[5]
    modules['lgns'][8][4][1][0] = script_params[5]
    modules['lgns'][8][5][1][0] = script_params[5]
    modules['lgns'][8][6][1][0] = script_params[5]
    modules['lgns'][8][7][1][0] = script_params[5]
    modules['lgns'][8][2][2][0] = script_params[5]
    modules['lgns'][8][2][3][0] = script_params[5]
    modules['lgns'][8][2][4][0] = script_params[5]
    modules['lgns'][8][2][5][0] = script_params[5]
    modules['lgns'][8][2][6][0] = script_params[5]
    modules['lgns'][8][2][7][0] = script_params[5]
    modules['lgns'][8][3][7][0] = script_params[5]
    modules['lgns'][8][4][7][0] = script_params[5]
    modules['lgns'][8][5][7][0] = script_params[5]
    modules['lgns'][8][6][7][0] = script_params[5]
    modules['lgns'][8][7][7][0] = script_params[5]

def forthStimulusNshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[1]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'n' shape
    modules['lgns'][8][2][1][0] = script_params[5]
    modules['lgns'][8][3][1][0] = script_params[5]
    modules['lgns'][8][4][1][0] = script_params[5]
    modules['lgns'][8][5][1][0] = script_params[5]
    modules['lgns'][8][6][1][0] = script_params[5]
    modules['lgns'][8][7][1][0] = script_params[5]
    modules['lgns'][8][2][2][0] = script_params[5]
    modules['lgns'][8][2][3][0] = script_params[5]
    modules['lgns'][8][2][4][0] = script_params[5]
    modules['lgns'][8][2][5][0] = script_params[5]
    modules['lgns'][8][2][6][0] = script_params[5]
    modules['lgns'][8][2][7][0] = script_params[5]
    modules['lgns'][8][3][7][0] = script_params[5]
    modules['lgns'][8][4][7][0] = script_params[5]
    modules['lgns'][8][5][7][0] = script_params[5]
    modules['lgns'][8][6][7][0] = script_params[5]
    modules['lgns'][8][7][7][0] = script_params[5]

def s1_up_01(modules, script_params):
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    modules['attna_c'][8][0][0][0] = script_params[0]
    modules['attna_re'][8][0][0][0] = script_params[0]
    modules['attna_b'][8][0][0][0] = script_params[1]
    modules['attna_s'][8][0][0][0] = script_params[0]
    
    modules['mgns'][8][0][41][0] = script_params[5]
    modules['mgns'][8][0][42][0] = script_params[5]

def s1_up_02(modules, script_params):
    
    
    modules['mgns'][8][0][41][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][42][0] = script_params[5]
    modules['mgns'][8][0][43][0] = script_params[5]

def s1_up_03(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][42][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][43][0] = script_params[5]
    modules['mgns'][8][0][44][0] = script_params[5]

def s1_up_04(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][43][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][44][0] = script_params[5]
    modules['mgns'][8][0][45][0] = script_params[5]

def s1_up_05(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][44][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][45][0] = script_params[5]
    modules['mgns'][8][0][46][0] = script_params[5]

def s1_up_06(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][45][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][46][0] = script_params[5]
    modules['mgns'][8][0][47][0] = script_params[5]

def s1_down_01(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][46][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][47][0] = script_params[5]
    modules['mgns'][8][0][46][0] = script_params[5]

def s1_down_02(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][47][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][46][0] = script_params[5]
    modules['mgns'][8][0][45][0] = script_params[5]

def s1_down_03(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][46][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][45][0] = script_params[5]
    modules['mgns'][8][0][44][0] = script_params[5]

def s1_down_04(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][45][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][44][0] = script_params[5]
    modules['mgns'][8][0][43][0] = script_params[5]

def s1_down_05(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][44][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][43][0] = script_params[5]
    modules['mgns'][8][0][42][0] = script_params[5]

def s1_down_06(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][43][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][42][0] = script_params[5]
    modules['mgns'][8][0][41][0] = script_params[5]
##

def s2_up_01(modules, script_params):
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    modules['attna_c'][8][0][0][0] = script_params[0]
    modules['attna_re'][8][0][0][0] = script_params[0]
    modules['attna_b'][8][0][0][0] = script_params[0]
    modules['attna_s'][8][0][0][0] = script_params[1]
    
    modules['mgns'][8][0][41][0] = script_params[5]
    modules['mgns'][8][0][42][0] = script_params[5]

def s2_up_02(modules, script_params):
    
    
    modules['mgns'][8][0][41][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][42][0] = script_params[5]
    modules['mgns'][8][0][43][0] = script_params[5]

def s2_up_03(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][42][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][43][0] = script_params[5]
    modules['mgns'][8][0][44][0] = script_params[5]

def s2_up_04(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][43][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][44][0] = script_params[5]
    modules['mgns'][8][0][45][0] = script_params[5]

def s2_up_05(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][44][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][45][0] = script_params[5]
    modules['mgns'][8][0][46][0] = script_params[5]

def s2_up_06(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][45][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][46][0] = script_params[5]
    modules['mgns'][8][0][47][0] = script_params[5]

def s2_down_01(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][46][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][47][0] = script_params[5]
    modules['mgns'][8][0][46][0] = script_params[5]

def s2_down_02(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][47][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][46][0] = script_params[5]
    modules['mgns'][8][0][45][0] = script_params[5]

def s2_down_03(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][46][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][45][0] = script_params[5]
    modules['mgns'][8][0][44][0] = script_params[5]

def s2_down_04(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][45][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][44][0] = script_params[5]
    modules['mgns'][8][0][43][0] = script_params[5]

def s2_down_05(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][44][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][43][0] = script_params[5]
    modules['mgns'][8][0][42][0] = script_params[5]

def s2_down_06(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][43][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][42][0] = script_params[5]
    modules['mgns'][8][0][41][0] = script_params[5]
##

def s4_up_01(modules, script_params):
    """
        generates an up sweep to neural network using the given parameters
        
        """
    modules['attna_c'][8][0][0][0] = script_params[0]
    modules['attna_a'][8][0][0][0] = script_params[0]
    modules['attna_b'][8][0][0][0] = script_params[0]
    modules['attna_s'][8][0][0][0] = script_params[1]
    
    modules['mgns'][8][0][41][0] = script_params[3]
    modules['mgns'][8][0][42][0] = script_params[3]

def s4_up_02(modules, script_params):
    
    
    modules['mgns'][8][0][41][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][42][0] = script_params[3]
    modules['mgns'][8][0][43][0] = script_params[3]

def s4_up_03(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][42][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][43][0] = script_params[3]
    modules['mgns'][8][0][44][0] = script_params[3]

def s4_up_04(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][43][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][44][0] = script_params[3]
    modules['mgns'][8][0][45][0] = script_params[3]

def s4_up_05(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][44][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][45][0] = script_params[3]
    modules['mgns'][8][0][46][0] = script_params[3]

def s4_up_06(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][45][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][46][0] = script_params[3]
    modules['mgns'][8][0][47][0] = script_params[3]

def s4_down_01(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][46][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][47][0] = script_params[3]
    modules['mgns'][8][0][46][0] = script_params[3]

def s4_down_02(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][47][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][46][0] = script_params[3]
    modules['mgns'][8][0][45][0] = script_params[3]

def s4_down_03(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][46][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][45][0] = script_params[3]
    modules['mgns'][8][0][44][0] = script_params[3]

def s4_down_04(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][45][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][44][0] = script_params[3]
    modules['mgns'][8][0][43][0] = script_params[3]

def s4_down_05(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][44][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][43][0] = script_params[3]
    modules['mgns'][8][0][42][0] = script_params[3]

def s4_down_06(modules, script_params):
    
    modules['mgns'][8][0][43][0] = 0.
    
    modules['mgns'][8][0][42][0] = script_params[3]
    modules['mgns'][8][0][41][0] = script_params[3]

def s3_up_01(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    modules['attna_c'][8][0][0][0] = script_params[1]
    modules['attna_a'][8][0][0][0] = script_params[0]
    modules['attna_b'][8][0][0][0] = script_params[0]
    modules['attna_s'][8][0][0][0] = script_params[0]
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][41][0] = script_params[3]
    modules['mgns'][8][0][42][0] = script_params[3]

def s3_up_02(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    modules['mgns'][8][0][41][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][42][0] = script_params[3]
    modules['mgns'][8][0][43][0] = script_params[3]

def s3_up_03(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][42][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][43][0] = script_params[3]
    modules['mgns'][8][0][44][0] = script_params[3]

def s3_up_04(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][43][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][44][0] = script_params[3]
    modules['mgns'][8][0][45][0] = script_params[3]

def s3_up_05(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][44][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][45][0] = script_params[3]
    modules['mgns'][8][0][46][0] = script_params[3]

def s3_up_06(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][45][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][46][0] = script_params[3]
    modules['mgns'][8][0][47][0] = script_params[3]

def s3_down_01(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][46][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][47][0] = script_params[3]
    modules['mgns'][8][0][46][0] = script_params[3]

def s3_down_02(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][47][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][46][0] = script_params[3]
    modules['mgns'][8][0][45][0] = script_params[3]

def s3_down_03(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][46][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][45][0] = script_params[3]
    modules['mgns'][8][0][44][0] = script_params[3]

def s3_down_04(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    # reset previous activation
    modules['mgns'][8][0][45][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][44][0] = script_params[3]
    modules['mgns'][8][0][43][0] = script_params[3]

def s3_down_05(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][44][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][43][0] = script_params[3]
    modules['mgns'][8][0][42][0] = script_params[3]

def s3_down_06(modules, script_params):
    
    """
        generates an up sweep to neural network using the given parameters
        
        """
    # reset previous activation
    modules['mgns'][8][0][43][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][42][0] = script_params[3]
    modules['mgns'][8][0][41][0] = script_params[3]


simulation_events = {
    '0': intertrial_interval,
    '20': intertrial_interval,
    
    '99': firstStimulusUshape,
    '100': s1_up_01,
    '120': s1_up_02,
    '140': s1_up_03,
    '160': s1_up_04,
    '180': s1_up_05,
    '200': s1_up_06,
    '220': s1_down_01,
    '240': s1_down_02,
    '260': s1_down_03,
    '280': s1_down_04,
    '300': s1_down_05,
    '320': s1_down_06,
        '340': delay_period,

    '839': secondStimulusUshape,
    '840': s2_up_01,
    '860': s2_up_02,
    '880': s2_up_03,
    '900': s2_up_04,
    '920': s2_up_05,
    '940': s2_up_06,
    '960': s2_down_01,
    '980': s2_down_02,
    '1000': s2_down_03,
    '1020': s2_down_04,
    '1040': s2_down_05,
    '1060': s2_down_06,
    '1080': delay_period,

'1180': intertrial_interval,
    
    '1679': firstStimulusUshape,
    '1680': s1_up_01,
    '1700': s1_up_02,
    '1720': s1_up_03,
    '1740': s1_up_04,
    '1760': s1_up_05,
    '1780': s1_up_06,
    '1800': s1_down_01,
    '1820': s1_down_02,
    '1840': s1_down_03,
    '1860': s1_down_04,
    '1880': s1_down_05,
    '1900': s1_down_06,
    '1920': delay_period,
    
    '2419': secondStimulusUshape,
    '2420': s2_up_01,
    '2440': s2_up_02,
    '2460': s2_up_03,
    '2480': s2_up_04,
    '2500': s2_up_05,
    '2520': s2_up_06,
    '2560': s2_down_01,
    '2580': s2_down_02,
    '2600': s2_down_03,
    '2620': s2_down_04,
    '2640': s2_down_05,
    '2660': s2_down_06,
    '2680': delay_period,
    
    '2780': intertrial_interval,
    
    '3279': thirdStimulusNshape,
    '3280': s3_up_01,
    '3300': s3_up_02,
    '3320': s3_up_03,
    '3340': s3_up_04,
    '3360': s3_up_05,
    '3380': s3_up_06,
    '3400': s3_down_01,
    '3420': s3_down_02,
    '3440': s3_down_03,
    '3460': s3_down_04,
    '3480': s3_down_05,
    '3500': s3_down_06,
    '3520': delay_period,
    
    '4019': forthStimulusNshape,
    '4020': s4_up_01,
    '4040': s4_up_02,
    '4060': s4_up_03,
    '4080': s4_up_04,
    '4100': s4_up_05,
    '4120': s4_up_06,
    '4160': s4_down_01,
    '4180': s4_down_02,
    '4200': s4_down_03,
    '4220': s4_down_04,
    '4240': s4_down_05,
    '4260': s4_down_06,
    '4280': delay_period,
    
    '4380': intertrial_interval,
    '4390': intertrial_interval
}


