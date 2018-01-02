#!/usr/bin/python
#
# The following script replicates the results of Horwitz, Warner et al (2005), Figure 3.
#
# There are 6 trials total: 3 DMS trials and 3 control trials
#
# Total number of timesteps is 6600 = 33 seconds
#
# The number of timesteps in each trial is 1100 = 5.5 seconds
#
# The DMS trials are MATCH, MISMATCH, MATCH. The attention parameter in DMS trials is 0.3
# The control trials are 'passive viewing': random shapes are presented and low attention (0.05)
# is used. Passive viewing trials are also organized as MATCH, MISMATCH, MATCH.
#
# The first 200 timesteps = 1000 ms we do nothing. We assume 1 timestep = 5 ms, as in Horwitz
# et al (2005)
#
# To maintain consistency with Husain et al (2004) and Tagamets and Horwitz (1998),
# we are assuming that each simulation timestep is equivalent to 5 milliseconds
# of real time. 
                
# now we present S1 by manually inserting it into the MGN module and leaving S1 there
# for 200 timesteps (1 second).

# define the simulation time in total number of timesteps
# Each timestep is roughly equivalent to 5ms
LSNM_simulation_time = 85000
                
# Define list of parameters the the script is going to need to modify the LSNM neural network
# They are organized in the following order:
# [lo_att_level, hi_att_level, lo_inp_level, hi_inp_level, att_step, ri1, ri2]
script_params = [0.0, 0.3, 0.05, 0.7, 0.02, [], [],0.05]

# the following is random shape1, this shape has the same luminance as an 'O'
rand_shape1 = rdm.sample(range(81),18)
rand_indeces1 = np.unravel_index(rand_shape1,(9,9))
script_params[5] = zip(*rand_indeces1)

# A second random shape in inserted for a mismatch
rand_shape2 = rdm.sample(range(81),18)
rand_indeces2 = np.unravel_index(rand_shape2,(9,9))
script_params[6] = zip(*rand_indeces2)
        

def firstStimulusUshape(modules, script_params):
    
    """
    generates a u-shaped visual input to neural network with parameters given"
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[1]
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

def secondStimulusNshape(modules, script_params):
    
    """
    generates a n-shaped visual input to neural network with parameters given"
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[1]
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

def secondStimulusNshape_L(modules, script_params):
    
    """
    generates a n-shaped visual input to neural network with parameters given"
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[7]
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
 
def thirdStimulusNshape_L(modules, script_params):
    
    """
    generates a n-shaped visual input to neural network with parameters given"
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[7]
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

def thirdStimulusCshape(modules, script_params):
    
    """
    generates a n-shaped visual input to neural network with parameters given"
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[1]
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
    modules['lgns'][8][7][2][0] = script_params[3]
    modules['lgns'][8][7][3][0] = script_params[3]
    modules['lgns'][8][7][4][0] = script_params[3]
    modules['lgns'][8][7][5][0] = script_params[3]
    modules['lgns'][8][7][6][0] = script_params[3]
    modules['lgns'][8][7][7][0] = script_params[3]

def thirdStimulusCshape_L(modules, script_params):
    
    """
    generates a n-shaped visual input to neural network with parameters given"
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[7]
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
    modules['lgns'][8][7][2][0] = script_params[3]
    modules['lgns'][8][7][3][0] = script_params[3]
    modules['lgns'][8][7][4][0] = script_params[3]
    modules['lgns'][8][7][5][0] = script_params[3]
    modules['lgns'][8][7][6][0] = script_params[3]
    modules['lgns'][8][7][7][0] = script_params[3]

def random_shape_1(modules, script_params):
    """
    generates a random visual input to neural network with parameters given
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[1]
    modules['attnv_s'][8][0][0][0] = script_params[0]

    for k1 in range(len(script_params[5])):
        modules['lgns'][8][script_params[5][k1][0]][script_params[5][k1][1]][0] = script_params[3]
    
def random_shape_2(modules, script_params):
    """
    generates a random visual input to neural network with parameters given
    
    """
    
    modules['attnv'][8][0][0][0] = script_params[0]

    for k1 in range(len(script_params[6])):
        modules['lgns'][8][script_params[6][k1][0]][script_params[6][k1][1]][0] = script_params[3]

def lastStimulusUshape(modules, script_params):
    
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
    
def delay_period(modules, script_params):
    
    """
        modifies neural network with delay period parameters given
        
        """
    
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['lgns'][0]):
        for y in range(modules['lgns'][1]):
            modules['lgns'][8][x][y][0] = script_params[2]
    #modules['attnv'][8][0][0][0] = script_params[1]
    #change the endogenous attention to low, leave the exo attention as it is.
    modules['attnv_re'][8][0][0][0] = script_params[2]
    modules['attnv_a'][8][0][0][0] = script_params[2]
    modules['attnv_b'][8][0][0][0] = script_params[2]
    modules['attnv_s'][8][0][0][0] = script_params[2]
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['mgns'][0]):
        for y in range(modules['mgns'][1]):
            modules['mgns'][8][x][y][0] = script_params[2]
    #modules['attna_a'][8][0][0][0] = script_params[6]
    modules['attna_re'][8][0][0][0] = script_params[2]
    modules['attna_c'][8][0][0][0] = script_params[2]
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
    #modules['attnv'][8][0][0][0] = script_params[0]
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attna_re'][8][0][0][0] = script_params[0]
    #modules['attna_a'][8][0][0][0] = script_params[0]
    modules['attna_b'][8][0][0][0] = script_params[0]
    modules['attna_s'][8][0][0][0] = script_params[0]
    modules['attna_c'][8][0][0][0] = script_params[0]

def increase_attention(modules, script_params):
    """
    Increases 'hi_att_level' by a step given by 'att_step'

    """

    script_params[1] = script_params[1] + script_params[4]

#############################################################################
#ctrl task defined below

def firstStimulusdUshape(modules, script_params):
    
    """
    generates a u-shaped visual input to neural network with parameters given"
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[7]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][0][1][0] = script_params[3]
    modules['lgns'][8][3][4][0] = script_params[3]
    modules['lgns'][8][5][2][0] = script_params[3]
    modules['lgns'][8][5][1][0] = script_params[3]
    modules['lgns'][8][6][3][0] = script_params[3]
    modules['lgns'][8][8][0][0] = script_params[3]
    modules['lgns'][8][5][6][0] = script_params[3]
    modules['lgns'][8][7][3][0] = script_params[3]
    modules['lgns'][8][8][4][0] = script_params[3]
    modules['lgns'][8][2][4][0] = script_params[3]
    modules['lgns'][8][7][8][0] = script_params[3]
    modules['lgns'][8][0][8][0] = script_params[3]
    modules['lgns'][8][2][5][0] = script_params[3]
    modules['lgns'][8][4][8][0] = script_params[3]
    modules['lgns'][8][4][4][0] = script_params[3]
    modules['lgns'][8][6][6][0] = script_params[3]
    modules['lgns'][8][8][8][0] = script_params[3]

def secondStimulusdNshape(modules, script_params):
    
    """
    generates a n-shaped visual input to neural network with parameters given"
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[7]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]

    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'n' shape
    modules['lgns'][8][3][0][0] = script_params[3]
    modules['lgns'][8][2][2][0] = script_params[3]
    modules['lgns'][8][3][1][0] = script_params[3]
    modules['lgns'][8][5][3][0] = script_params[3]
    modules['lgns'][8][6][2][0] = script_params[3]
    modules['lgns'][8][6][0][0] = script_params[3]
    modules['lgns'][8][0][0][0] = script_params[3]
    modules['lgns'][8][3][0][0] = script_params[3]
    modules['lgns'][8][2][4][0] = script_params[3]
    modules['lgns'][8][0][5][0] = script_params[3]
    modules['lgns'][8][4][5][0] = script_params[3]
    modules['lgns'][8][2][8][0] = script_params[3]
    modules['lgns'][8][3][4][0] = script_params[3]
    modules['lgns'][8][5][7][0] = script_params[3]
    modules['lgns'][8][5][1][0] = script_params[3]
    modules['lgns'][8][6][6][0] = script_params[3]
    modules['lgns'][8][8][8][0] = script_params[3]
 
def thirdStimulusdCshape(modules, script_params):
    
    """
    generates a n-shaped visual input to neural network with parameters given"
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[7]
    modules['attnv_s'][8][0][0][0] = script_params[0]

    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'n' shape
    modules['lgns'][8][0][1][0] = script_params[3]
    modules['lgns'][8][3][5][0] = script_params[3]
    modules['lgns'][8][4][1][0] = script_params[3]
    modules['lgns'][8][4][2][0] = script_params[3]
    modules['lgns'][8][6][0][0] = script_params[3]
    modules['lgns'][8][8][1][0] = script_params[3]
    modules['lgns'][8][4][2][0] = script_params[3]
    modules['lgns'][8][1][3][0] = script_params[3]
    modules['lgns'][8][1][5][0] = script_params[3]
    modules['lgns'][8][0][5][0] = script_params[3]
    modules['lgns'][8][3][5][0] = script_params[3]
    modules['lgns'][8][2][7][0] = script_params[3]
    modules['lgns'][8][6][1][0] = script_params[3]
    modules['lgns'][8][7][2][0] = script_params[3]
    modules['lgns'][8][6][3][0] = script_params[3]
    modules['lgns'][8][5][5][0] = script_params[3]
    modules['lgns'][8][8][8][0] = script_params[3]
    modules['lgns'][8][8][5][0] = script_params[3]

def lastStimulusdUshape(modules, script_params):
    
    """
    generates a u-shaped visual input to neural network with parameters given"
    
    """
    modules['attnv_re'][8][0][0][0] = script_params[0]
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[7]
    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'U' shape
    modules['lgns'][8][0][0][0] = script_params[3]
    modules['lgns'][8][3][1][0] = script_params[3]
    modules['lgns'][8][4][3][0] = script_params[3]
    modules['lgns'][8][5][2][0] = script_params[3]
    modules['lgns'][8][5][0][0] = script_params[3]
    modules['lgns'][8][8][0][0] = script_params[3]
    modules['lgns'][8][6][2][0] = script_params[3]
    modules['lgns'][8][7][3][0] = script_params[3]
    modules['lgns'][8][8][3][0] = script_params[3]
    modules['lgns'][8][8][5][0] = script_params[3]
    modules['lgns'][8][7][8][0] = script_params[3]
    modules['lgns'][8][2][8][0] = script_params[3]
    modules['lgns'][8][1][6][0] = script_params[3]
    modules['lgns'][8][4][8][0] = script_params[3]
    modules['lgns'][8][5][5][0] = script_params[3]
    modules['lgns'][8][6][6][0] = script_params[3]
    modules['lgns'][8][7][5][0] = script_params[3]

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
    
# define a dictionary of simulation events functions, each associated with
# a specific simulation timestep
simulation_events = {        
    '20': intertrial_interval,
#DMS
    '200': firstStimulusUshape,                

    '600': delay_period,
    
    '3820': s4_up_01,
    '3840': s4_up_02,
    '3860': s4_up_03,
    '3880': s4_up_04,
    '3900': s4_up_05,
    '3920': s4_up_06,
    '3940': s4_down_01,
    '3960': s4_down_02,
    '3980': s4_down_03,
    '4000': s4_down_04,
    '4020': s4_down_05,
    '4040': s4_down_06,

    '4600': lastStimulusUshape,

    '5000': delay_period,
    '5005': intertrial_interval,
    '5010': intertrial_interval

}


##- EoF -##
