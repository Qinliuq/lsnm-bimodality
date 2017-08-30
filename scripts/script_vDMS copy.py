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


# define the simulation time in total number of timesteps
# Each timestep is roughly equivalent to 5ms
LSNM_simulation_time = 42000 #210 seconds.
                
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
    
    modules['attnv_re'][8][0][0][0] = script_params[0]

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
    
    
def delay_period(modules, script_params):
    
    """
    modifies neural network with delay period parameters given

    """
    
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['lgns'][0]):
        for y in range(modules['lgns'][1]):
            modules['lgns'][8][x][y][0] = script_params[2]
    modules['attnv_re'][8][0][0][0] = script_params[2]



def intertrial_interval(modules, script_params):
    """
    resets the visual inputs and short-term memory using given parameters

    """

    # reset D1
    for x in range(modules['evd1'][0]):
        for y in range(modules['evd1'][1]):
            modules['evd1'][8][x][y][0] = script_params[2]
    for x in range(modules['evd2'][0]):
        for y in range(modules['evd2'][1]):
            modules['evd2'][8][x][y][0] = script_params[2]

    for x in range(modules['evd1_a'][0]):
        for y in range(modules['evd1_a'][1]):
            modules['evd1_a'][8][x][y][0] = script_params[2]
    for x in range(modules['evd2_a'][0]):
        for y in range(modules['evd2_a'][1]):
            modules['evd2_a'][8][x][y][0] = script_params[2]

    for x in range(modules['evd1_b'][0]):
        for y in range(modules['evd1_b'][1]):
            modules['evd1_b'][8][x][y][0] = script_params[2]
    for x in range(modules['evd2_b'][0]):
        for y in range(modules['evd2_b'][1]):
            modules['evd2_b'][8][x][y][0] = script_params[2]

    for x in range(modules['evd1_s'][0]):
        for y in range(modules['evd1_s'][1]):
            modules['evd1_s'][8][x][y][0] = script_params[2]	
    for x in range(modules['evd2_s'][0]):
        for y in range(modules['evd2_s'][1]):
            modules['evd2_s'][8][x][y][0] = script_params[2]    
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['lgns'][0]):
        for y in range(modules['lgns'][1]):
            modules['lgns'][8][x][y][0] = script_params[2]

    # turn attention to 'LO', as the current trial has ended
    modules['attnv_a'][8][0][0][0] = script_params[0]
    modules['attnv_b'][8][0][0][0] = script_params[0]
    modules['attnv_s'][8][0][0][0] = script_params[0]
    modules['attnv_re'][8][0][0][0] = script_params[2]

def increase_attention(modules, script_params):
    """
    Increases 'hi_att_level' by a step given by 'att_step'

    """

    script_params[1] = script_params[1] + script_params[4]

    
# define a dictionary of simulation events functions, each associated with
# a specific simulation timestep
simulation_events = {        
    '20': intertrial_interval,
# block 1, DMS test
    '1200': firstStimulusUshape,   
    '1400': delay_period,
    '2200': firstStimulusUshape,
    '2400': intertrial_interval,

    '3400': firstStimulusUshape,
    '3600': delay_period,
    '4400': firstStimulusUshape,
    '4600': intertrial_interval,

    '5600': firstStimulusUshape,
    '5800': delay_period,
    '6600': firstStimulusUshape,
    '6800': intertrial_interval,

# block 2, control task
    '7800': firstStimulusdUshape,
    '8000': delay_period,
    '8800': firstStimulusdUshape,
    '9000': intertrial_interval,

    '10000': firstStimulusdUshape,
    '10200': delay_period,
    '11000': firstStimulusdUshape,
    '11200': intertrial_interval,

    '12200': firstStimulusdUshape,
    '12400': delay_period,
    '13200': firstStimulusdUshape,
    '13400': intertrial_interval,

#block 3: DMS
    '14400': firstStimulusUshape,   
    '14600': delay_period,
    '15400': firstStimulusUshape,
    '15600': intertrial_interval,

    '16600': firstStimulusUshape,
    '16800': delay_period,
    '17600': firstStimulusUshape,
    '17800': intertrial_interval,

    '18800': firstStimulusUshape,
    '19000': delay_period,
    '19800': firstStimulusUshape,
    '20000': intertrial_interval,

# block 4: ctrl
    '21000': firstStimulusdUshape,
    '21200': delay_period,
    '22000': firstStimulusdUshape,
    '22200': intertrial_interval,

    '23200': firstStimulusdUshape,
    '23400': delay_period,
    '24200': firstStimulusdUshape,
    '24400': intertrial_interval,

    '25400': firstStimulusdUshape,
    '25600': delay_period,
    '26400': firstStimulusdUshape,
    '26600': intertrial_interval,

# block 5: DMS
    '27600': firstStimulusUshape,   
    '27800': delay_period,
    '28600': firstStimulusUshape,
    '28800': intertrial_interval,

    '29800': firstStimulusUshape,
    '30000': delay_period,
    '30800': firstStimulusUshape,
    '31000': intertrial_interval,

    '32000': firstStimulusUshape,
    '32200': delay_period,
    '33000': firstStimulusUshape,
    '33200': intertrial_interval,

# block 6: ctrl
    '34200': firstStimulusdUshape,
    '34400': delay_period,
    '35200': firstStimulusdUshape,
    '35400': intertrial_interval,

    '36400': firstStimulusdUshape,
    '36600': delay_period,
    '37400': firstStimulusdUshape,
    '37600': intertrial_interval,

    '38600': firstStimulusdUshape,
    '38800': delay_period,
    '39600': firstStimulusdUshape,
    '39800': intertrial_interval,

    '40000': intertrial_interval


}


##- EoF -##
