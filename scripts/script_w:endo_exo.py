#!/usr/bin/python
#
# The following script implements visual-auditory bimodal DMS trials with both endogenours and exogenous attention.
#
# There are 5 trials in each modality running simutaneously: 5 visual DMS trials and 5 auditory DMS trials.
#
# The endogenous attention is set to attend auditory stimuli, the exogenous attention is coupled with the saliency of inputs.
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
LSNM_simulation_time = 7200

# Define list of parameters the script is going to need to modify the LSNM neural network
# They are organized in the following order:
# [lo_att_level, hi_att_level, lo_inp_level, hi_inp_level, att_step, ri1, ri2]

script_params = [0.0, 0.05, 0.1, 0.3, 0.5, 0.7, 0.9]

def delay_period(modules, script_params):
    
    """
        modifies neural network with delay period parameters given
        
        """
    
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['lgns'][0]):
        for y in range(modules['lgns'][1]):
            modules['lgns'][8][x][y][0] = script_params[1]
    #modules['attnv'][8][0][0][0] = script_params[1]
    #change the endogenous attention to low, leave the exo attention as it is.
    modules['attnv_re'][8][0][0][0] = script_params[1]
    modules['attnv_a'][8][0][0][0] = script_params[1]
    modules['attnv_b'][8][0][0][0] = script_params[1]
    modules['attnv_s'][8][0][0][0] = script_params[1]
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['mgns'][0]):
        for y in range(modules['mgns'][1]):
            modules['mgns'][8][x][y][0] = script_params[1]
    #modules['attna_a'][8][0][0][0] = script_params[6]
    modules['attna_re'][8][0][0][0] = script_params[1]
    modules['attna_c'][8][0][0][0] = script_params[1]
    modules['attna_b'][8][0][0][0] = script_params[1]
    modules['attna_s'][8][0][0][0] = script_params[1]

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
    #modules['attnv'][8][0][0][0] = script_params[0]
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attna_re'][8][0][0][0] = script_params[0]
    #modules['attna_a'][8][0][0][0] = script_params[0]
    modules['attna_b'][8][0][0][0] = script_params[0]
    modules['attna_s'][8][0][0][0] = script_params[0]
    modules['attna_c'][8][0][0][0] = script_params[0]

def firstStimulusUshape(modules, script_params):
    
    """
        generates a u-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][2][1][0] = script_params[2]
    modules['lgns'][8][3][1][0] = script_params[2]
    modules['lgns'][8][4][1][0] = script_params[2]
    modules['lgns'][8][5][1][0] = script_params[2]
    modules['lgns'][8][6][1][0] = script_params[2]
    modules['lgns'][8][7][1][0] = script_params[2]
    modules['lgns'][8][7][2][0] = script_params[2]
    modules['lgns'][8][7][3][0] = script_params[2]
    modules['lgns'][8][7][4][0] = script_params[2]
    modules['lgns'][8][7][5][0] = script_params[2]
    modules['lgns'][8][7][6][0] = script_params[2]
    modules['lgns'][8][2][7][0] = script_params[2]
    modules['lgns'][8][3][7][0] = script_params[2]
    modules['lgns'][8][4][7][0] = script_params[2]
    modules['lgns'][8][5][7][0] = script_params[2]
    modules['lgns'][8][6][7][0] = script_params[2]
    modules['lgns'][8][7][7][0] = script_params[2]

def secondStimulusUshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][2][1][0] = script_params[2]
    modules['lgns'][8][3][1][0] = script_params[2]
    modules['lgns'][8][4][1][0] = script_params[2]
    modules['lgns'][8][5][1][0] = script_params[2]
    modules['lgns'][8][6][1][0] = script_params[2]
    modules['lgns'][8][7][1][0] = script_params[2]
    modules['lgns'][8][7][2][0] = script_params[2]
    modules['lgns'][8][7][3][0] = script_params[2]
    modules['lgns'][8][7][4][0] = script_params[2]
    modules['lgns'][8][7][5][0] = script_params[2]
    modules['lgns'][8][7][6][0] = script_params[2]
    modules['lgns'][8][2][7][0] = script_params[2]
    modules['lgns'][8][3][7][0] = script_params[2]
    modules['lgns'][8][4][7][0] = script_params[2]
    modules['lgns'][8][5][7][0] = script_params[2]
    modules['lgns'][8][6][7][0] = script_params[2]
    modules['lgns'][8][7][7][0] = script_params[2]

def thirdStimulusUshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
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

def forthStimulusUshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
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

def fifthStimulusUshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][2][1][0] = script_params[4]
    modules['lgns'][8][3][1][0] = script_params[4]
    modules['lgns'][8][4][1][0] = script_params[4]
    modules['lgns'][8][5][1][0] = script_params[4]
    modules['lgns'][8][6][1][0] = script_params[4]
    modules['lgns'][8][7][1][0] = script_params[4]
    modules['lgns'][8][7][2][0] = script_params[4]
    modules['lgns'][8][7][3][0] = script_params[4]
    modules['lgns'][8][7][4][0] = script_params[4]
    modules['lgns'][8][7][5][0] = script_params[4]
    modules['lgns'][8][7][6][0] = script_params[4]
    modules['lgns'][8][2][7][0] = script_params[4]
    modules['lgns'][8][3][7][0] = script_params[4]
    modules['lgns'][8][4][7][0] = script_params[4]
    modules['lgns'][8][5][7][0] = script_params[4]
    modules['lgns'][8][6][7][0] = script_params[4]
    modules['lgns'][8][7][7][0] = script_params[4]


def sixthStimulusUshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][2][1][0] = script_params[4]
    modules['lgns'][8][3][1][0] = script_params[4]
    modules['lgns'][8][4][1][0] = script_params[4]
    modules['lgns'][8][5][1][0] = script_params[4]
    modules['lgns'][8][6][1][0] = script_params[4]
    modules['lgns'][8][7][1][0] = script_params[4]
    modules['lgns'][8][7][2][0] = script_params[4]
    modules['lgns'][8][7][3][0] = script_params[4]
    modules['lgns'][8][7][4][0] = script_params[4]
    modules['lgns'][8][7][5][0] = script_params[4]
    modules['lgns'][8][7][6][0] = script_params[4]
    modules['lgns'][8][2][7][0] = script_params[4]
    modules['lgns'][8][3][7][0] = script_params[4]
    modules['lgns'][8][4][7][0] = script_params[4]
    modules['lgns'][8][5][7][0] = script_params[4]
    modules['lgns'][8][6][7][0] = script_params[4]
    modules['lgns'][8][7][7][0] = script_params[4]


def seventhStimulusUshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][2][1][0] = script_params[5]
    modules['lgns'][8][3][1][0] = script_params[5]
    modules['lgns'][8][4][1][0] = script_params[5]
    modules['lgns'][8][5][1][0] = script_params[5]
    modules['lgns'][8][6][1][0] = script_params[5]
    modules['lgns'][8][7][1][0] = script_params[5]
    modules['lgns'][8][7][2][0] = script_params[5]
    modules['lgns'][8][7][3][0] = script_params[5]
    modules['lgns'][8][7][4][0] = script_params[5]
    modules['lgns'][8][7][5][0] = script_params[5]
    modules['lgns'][8][7][6][0] = script_params[5]
    modules['lgns'][8][2][7][0] = script_params[5]
    modules['lgns'][8][3][7][0] = script_params[5]
    modules['lgns'][8][4][7][0] = script_params[5]
    modules['lgns'][8][5][7][0] = script_params[5]
    modules['lgns'][8][6][7][0] = script_params[5]
    modules['lgns'][8][7][7][0] = script_params[5]


def eighthStimulusUshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][2][1][0] = script_params[5]
    modules['lgns'][8][3][1][0] = script_params[5]
    modules['lgns'][8][4][1][0] = script_params[5]
    modules['lgns'][8][5][1][0] = script_params[5]
    modules['lgns'][8][6][1][0] = script_params[5]
    modules['lgns'][8][7][1][0] = script_params[5]
    modules['lgns'][8][7][2][0] = script_params[5]
    modules['lgns'][8][7][3][0] = script_params[5]
    modules['lgns'][8][7][4][0] = script_params[5]
    modules['lgns'][8][7][5][0] = script_params[5]
    modules['lgns'][8][7][6][0] = script_params[5]
    modules['lgns'][8][2][7][0] = script_params[5]
    modules['lgns'][8][3][7][0] = script_params[5]
    modules['lgns'][8][4][7][0] = script_params[5]
    modules['lgns'][8][5][7][0] = script_params[5]
    modules['lgns'][8][6][7][0] = script_params[5]
    modules['lgns'][8][7][7][0] = script_params[5]


def ninethStimulusUshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][2][1][0] = script_params[6]
    modules['lgns'][8][3][1][0] = script_params[6]
    modules['lgns'][8][4][1][0] = script_params[6]
    modules['lgns'][8][5][1][0] = script_params[6]
    modules['lgns'][8][6][1][0] = script_params[6]
    modules['lgns'][8][7][1][0] = script_params[6]
    modules['lgns'][8][7][2][0] = script_params[6]
    modules['lgns'][8][7][3][0] = script_params[6]
    modules['lgns'][8][7][4][0] = script_params[6]
    modules['lgns'][8][7][5][0] = script_params[6]
    modules['lgns'][8][7][6][0] = script_params[6]
    modules['lgns'][8][2][7][0] = script_params[6]
    modules['lgns'][8][3][7][0] = script_params[6]
    modules['lgns'][8][4][7][0] = script_params[6]
    modules['lgns'][8][5][7][0] = script_params[6]
    modules['lgns'][8][6][7][0] = script_params[6]
    modules['lgns'][8][7][7][0] = script_params[6]


def tenthStimulusUshape(modules, script_params):
    
    """
        generates a n-shaped visual input to neural network with parameters given"
        
        """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][2][1][0] = script_params[6]
    modules['lgns'][8][3][1][0] = script_params[6]
    modules['lgns'][8][4][1][0] = script_params[6]
    modules['lgns'][8][5][1][0] = script_params[6]
    modules['lgns'][8][6][1][0] = script_params[6]
    modules['lgns'][8][7][1][0] = script_params[6]
    modules['lgns'][8][7][2][0] = script_params[6]
    modules['lgns'][8][7][3][0] = script_params[6]
    modules['lgns'][8][7][4][0] = script_params[6]
    modules['lgns'][8][7][5][0] = script_params[6]
    modules['lgns'][8][7][6][0] = script_params[6]
    modules['lgns'][8][2][7][0] = script_params[6]
    modules['lgns'][8][3][7][0] = script_params[6]
    modules['lgns'][8][4][7][0] = script_params[6]
    modules['lgns'][8][5][7][0] = script_params[6]
    modules['lgns'][8][6][7][0] = script_params[6]
    modules['lgns'][8][7][7][0] = script_params[6]


def s1_up_01(modules, script_params):
    """
        generates an up sweep to neural network using the given parameters
        
        """
    
    modules['attna_c'][8][0][0][0] = script_params[0]
    modules['attna_re'][8][0][0][0] = script_params[4]
    modules['attna_b'][8][0][0][0] = script_params[0]
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
    modules['attna_b'][8][0][0][0] = script_params[3]
    modules['attna_s'][8][0][0][0] = script_params[0]
    
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
    modules['attna_re'][8][0][0][0] = script_params[0]
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
    modules['attna_re'][8][0][0][0] = script_params[0]
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

    '819': secondStimulusUshape,
    '820': s1_up_01,
    '840': s1_up_02,
    '860': s1_up_03,
    '880': s1_up_04,
    '900': s1_up_05,
    '920': s1_up_06,
    '940': s1_down_01,
    '960': s1_down_02,
    '980': s1_down_03,
    '1000': s1_down_04,
    '1020': s1_down_05,
    '1040': s1_down_06,
    '1060': delay_period,

'1100': intertrial_interval,
'1110': intertrial_interval,
'1120': intertrial_interval,
    
    '1599': thirdStimulusUshape,
    '1600': s1_up_01,
    '1620': s1_up_02,
    '1640': s1_up_03,
    '1660': s1_up_04,
    '1680': s1_up_05,
    '1700': s1_up_06,
    '1720': s1_down_01,
    '1740': s1_down_02,
    '1760': s1_down_03,
    '1780': s1_down_04,
    '1800': s1_down_05,
    '1820': s1_down_06,
        '1840': delay_period,
    
    '2319': forthStimulusUshape,
    '2320': s1_up_01,
    '2340': s1_up_02,
    '2360': s1_up_03,
    '2380': s1_up_04,
    '2400': s1_up_05,
    '2420': s1_up_06,
    '2440': s1_down_01,
    '2460': s1_down_02,
    '2480': s1_down_03,
    '2500': s1_down_04,
    '2520': s1_down_05,
    '2540': s1_down_06,
    '2560': delay_period,
    
'2600': intertrial_interval,
'2610': intertrial_interval,
'2620': intertrial_interval,
    
    '3099': fifthStimulusUshape,
    '3100': s1_up_01,
    '3120': s1_up_02,
    '3140': s1_up_03,
    '3160': s1_up_04,
    '3180': s1_up_05,
    '3200': s1_up_06,
    '3220': s1_down_01,
    '3240': s1_down_02,
    '3260': s1_down_03,
    '3280': s1_down_04,
    '3300': s1_down_05,
    '3320': s1_down_06,
        '3340': delay_period,
    
    '3819': sixthStimulusUshape,
    '3820': s1_up_01,
    '3840': s1_up_02,
    '3860': s1_up_03,
    '3880': s1_up_04,
    '3900': s1_up_05,
    '3920': s1_up_06,
    '3940': s1_down_01,
    '3960': s1_down_02,
    '3980': s1_down_03,
    '4000': s1_down_04,
    '4020': s1_down_05,
    '4040': s1_down_06,
    '4060': delay_period,
    
'4100': intertrial_interval,
'4110': intertrial_interval,
'4120': intertrial_interval,
    
    
    '4599': seventhStimulusUshape,

    '4600': s1_up_01,
    '4620': s1_up_02,
    '4640': s1_up_03,
    '4660': s1_up_04,
    '4680': s1_up_05,
    '4700': s1_up_06,
    '4720': s1_down_01,
    '4740': s2_down_02,
    '4760': s2_down_03,
    '4780': s2_down_04,
    '4800': s2_down_05,
    '4820': s2_down_06,
    '4840': delay_period,

    '5319': eighthStimulusUshape,
    '5320': s1_up_01,
    '5340': s1_up_02,
    '5360': s1_up_03,
    '5380': s1_up_04,
    '5400': s1_up_05,
    '5420': s1_up_06,
    '5440': s1_down_01,
    '5460': s1_down_02,
    '5480': s1_down_03,
    '5400': s1_down_04,
    '5520': s1_down_05,
    '5540': s1_down_06,
        '5560': delay_period,

'5600': intertrial_interval,
'5610': intertrial_interval,
'5620': intertrial_interval,
    
    '6099': ninethStimulusUshape,

    '6100': s1_up_01,
    '6120': s1_up_02,
    '6140': s1_up_03,
    '6160': s1_up_04,
    '6180': s1_up_05,
    '6200': s1_up_06,
    '6220': s1_down_01,
    '6240': s1_down_02,
    '6260': s1_down_03,
    '6280': s1_down_04,
    '6300': s1_down_05,
    '6320': s1_down_06,
    '6340': delay_period,
    
    '6819': tenthStimulusUshape,
    '6820': s1_up_01,
    '6840': s1_up_02,
    '6860': s1_up_03,
    '6880': s1_up_04,
    '6900': s1_up_05,
    '6920': s1_up_06,
    '6940': s1_down_01,
    '6960': s1_down_02,
    '6980': s1_down_03,
    '7000': s1_down_04,
    '7020': s1_down_05,
    '7040': s1_down_06,
    '7060': delay_period,

'7100': intertrial_interval,
'7105': intertrial_interval,
'7110': intertrial_interval

}


