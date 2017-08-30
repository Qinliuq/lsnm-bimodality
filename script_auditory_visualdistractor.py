#!/usr/bin/python
#
# The following script is a test of the AV associated model.
#
# A list of stimuli (A/V) are shown. 
#
# Total number of timesteps is 5400. (200 time steps = 1 second)
#
LSNM_simulation_time = 3000

# Define list of parameters the script is going to need to modify the LSNM neural network
# They are organized in the following order:
# [lo_att_level, hi_att_level, lo_inp_level, hi_inp_level, att_step, ri1, ri2]

script_params = [0.0, 0.3, 0.05, 0.7, 0.02, [], [], 0.1]

def delay_period(modules, script_params):
    
    """
    modifies neural network with delay period parameters given

    """
    
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['lgns'][0]):
        for y in range(modules['lgns'][1]):
            modules['lgns'][8][x][y][0] = script_params[2]
    modules['attnv'][8][0][0][0] = script_params[7]
    modules['attnv_re'][8][0][0][0] = script_params[2]
    modules['attnv_a'][8][0][0][0] = script_params[2]
    modules['attnv_b'][8][0][0][0] = script_params[2]
    modules['attnv_s'][8][0][0][0] = script_params[2]
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['mgns'][0]):
        for y in range(modules['mgns'][1]):
            modules['mgns'][8][x][y][0] = script_params[2]
    modules['attna_c'][8][0][0][0] = script_params[2]
    modules['attna_a'][8][0][0][0] = script_params[7]
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
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]

    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'n' shape
    modules['lgns'][8][2][1][0] = script_params[3]
    modules['lgns'][8][3][1][0] = script_params[3]
    modules['lgns'][8][4][1][0] = script_params[3]
    modules['lgns'][8][5][1][0] = script_params[3]
    modules['lgns'][8][6][1][0] = script_params[3]
    modules['lgns'][8][7][1][0] = script_params[3]
    modules['lgns'][8][2][2][0] = script_params[3]
    modules['lgns'][8][2][3][0] = script_params[3]
    modules['lgns'][8][2][4][0] = script_params[3]
    modules['lgns'][8][2][5][0] = script_params[3]
    modules['lgns'][8][2][6][0] = script_params[3]
    modules['lgns'][8][2][7][0] = script_params[3]
    modules['lgns'][8][3][7][0] = script_params[3]
    modules['lgns'][8][4][7][0] = script_params[3]
    modules['lgns'][8][5][7][0] = script_params[3]
    modules['lgns'][8][6][7][0] = script_params[3]
    modules['lgns'][8][7][7][0] = script_params[3]
  

def LastStimulusUshape(modules, script_params):
    
    """
    generates a u-shaped visual input to neural network with parameters given"
    
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

def s1_up_01(modules, script_params):
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    modules['attna_c'][8][0][0][0] = script_params[0]
    modules['attna_a'][8][0][0][0] = script_params[0]
    modules['attna_b'][8][0][0][0] = script_params[1]
    modules['attna_s'][8][0][0][0] = script_params[0]

    modules['mgns'][8][0][41][0] = script_params[3]
    modules['mgns'][8][0][42][0] = script_params[3]

def s1_up_02(modules, script_params):
    

    modules['mgns'][8][0][41][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][42][0] = script_params[3]
    modules['mgns'][8][0][43][0] = script_params[3]

def s1_up_03(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """

    # reset previous activation
    modules['mgns'][8][0][42][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][43][0] = script_params[3]
    modules['mgns'][8][0][44][0] = script_params[3]

def s1_up_04(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][43][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][44][0] = script_params[3]
    modules['mgns'][8][0][45][0] = script_params[3]

def s1_up_05(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][44][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][45][0] = script_params[3]
    modules['mgns'][8][0][46][0] = script_params[3]

def s1_up_06(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    # reset previous activation
    modules['mgns'][8][0][45][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][46][0] = script_params[3]
    modules['mgns'][8][0][47][0] = script_params[3]

def s1_down_01(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][46][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][47][0] = script_params[3]
    modules['mgns'][8][0][46][0] = script_params[3]

def s1_down_02(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """

    # reset previous activation
    modules['mgns'][8][0][47][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][46][0] = script_params[3]
    modules['mgns'][8][0][45][0] = script_params[3]

def s1_down_03(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][46][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][45][0] = script_params[3]
    modules['mgns'][8][0][44][0] = script_params[3]

def s1_down_04(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][45][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][44][0] = script_params[3]
    modules['mgns'][8][0][43][0] = script_params[3]

def s1_down_05(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
        # reset previous activation
    modules['mgns'][8][0][44][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][43][0] = script_params[3]
    modules['mgns'][8][0][42][0] = script_params[3]

def s1_down_06(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
        # reset previous activation
    modules['mgns'][8][0][43][0] = 0.
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][42][0] = script_params[3]
    modules['mgns'][8][0][41][0] = script_params[3]
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

def s2_down_01(modules, script_params):
     
    """
    s2 can be used as the 2nd stimilus only; generates an up sweep to neural network using the given parameters
    
    """
    
    modules['attna_c'][8][0][0][0] = script_params[1]
    modules['attna_a'][8][0][0][0] = script_params[0]
    modules['attna_b'][8][0][0][0] = script_params[0]
    modules['attna_s'][8][0][0][0] = script_params[0] 

    modules['mgns'][8][0][59][0] = script_params[3]
    modules['mgns'][8][0][58][0] = script_params[3]
    

def s2_down_02(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """  
    
    modules['mgns'][8][0][59][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][58][0] = script_params[3]
    modules['mgns'][8][0][57][0] = script_params[3]

def s2_down_03(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][58][0] = 0.

    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][57][0] = script_params[3]
    modules['mgns'][8][0][56][0] = script_params[3]

def s2_down_04(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][57][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][56][0] = script_params[3]
    modules['mgns'][8][0][55][0] = script_params[3]

def s2_down_05(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][56][0] = 0.

    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][55][0] = script_params[3]
    modules['mgns'][8][0][54][0] = script_params[3]

def s2_down_06(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][55][0] = script_params[3]
    modules['mgns'][8][0][54][0] = script_params[3]
    
def s2_up_01(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][54][0] = script_params[3]
    modules['mgns'][8][0][55][0] = script_params[3]

def s2_up_02(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """

    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][55][0] = script_params[3]
    modules['mgns'][8][0][54][0] = script_params[3]

def s2_up_03(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][54][0] = 0.

    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][55][0] = script_params[3]
    modules['mgns'][8][0][56][0] = script_params[3]

def s2_up_04(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][55][0] = 0.
    
    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][56][0] = script_params[3]
    modules['mgns'][8][0][57][0] = script_params[3]

def s2_up_05(modules, script_params):
    
    """
    generates an up sweep to neural network using the given parameters
    
    """
    
    # reset previous activation
    modules['mgns'][8][0][56][0] = 0.

    # insert the inputs stimulus into MGN and see what happens
    # the following stimulus is an up sweep
    modules['mgns'][8][0][57][0] = script_params[3]
    modules['mgns'][8][0][58][0] = script_params[3]

def s2_up_06(modules, script_params):

    """
    generate an up sweep to neural network using the given params
    """

    modules['mgns'][8][0][57][0] = 0.

    modules['mgns'][8][0][58][0] = script_params[3]
    modules['mgns'][8][0][59][0] = script_params[3]

simulation_events = {        
    '0': intertrial_interval,            
    '20': intertrial_interval,

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
 
    '1580': thirdStimulusNshape,

        '1820': delay_period,

    '2320': s4_down_01,
   # '2321': thirdStimulusNshape,
    '2340': s4_down_02,
    '2360': s4_down_03,
    '2380': s4_down_04,
    '2400': s4_down_05,
    '2420': s4_down_06,
    '2440': s4_up_01,
    '2460': s4_up_02,
    '2480': s4_up_03,
    '2500': s4_up_04,
    '2520': s4_up_05,
    '2540': s4_up_06,
   
	'2560': intertrial_interval,
        '2570': intertrial_interval,
        '2600': intertrial_interval
}


##- EoF -##
