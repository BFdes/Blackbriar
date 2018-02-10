import numpy as np
import random as rnd
import matplotlib.pyplot as plt
#This version of the function is not vectorized. Explicitly does NOT use numpy facilites
def LS_v2(f, p_init, max_iter, bounds, radius, reduce_iter, reduce_frac, params=False):
    '''
    ---------------------
    Local Seach Algorithm
    ---------------------

    --- input ---

    f: objective function
    p_initi: initial point
    max_iter: maximum number of iterations
    bounds: bounds on the search domain
    radius: initial search radius
    reduce_iter: number of iterations with the same optimum that
        will induce a search radius reduction
    reduce_frac: fraction to which the search radius is reduced

    --- Notes ---

    1. This algorithm uses numpy arrays and tries to take advantage of vectorization.
    2. Make_plot decides whether to output all function evaluations
		or not.

    '''
    #initialization
    best_position = p_init
    best_value = f(p_init)
    dim = len(p_init)
    fail_count = 0
    # plotting utilities
    make_plot = params
    if dim < 1 and make_plot:
        print("warning, only 1 dimension, cannot plot")
    # creating arrays for the plots
    if make_plot:
        all_trials_x = np.zeros(max_iter)
        all_trials_y = np.zeros(max_iter)
        all_results = np.zeros(max_iter)
    #search loop
    for i_iter in range(max_iter):
        print('best_value = ',best_value,'   radius = ',radius)
        # tries random values in the vecinity of the best position so far
        p_trial = best_position + radius * np.array([rnd.uniform(bounds[i][0],bounds[i][1]) for i in range(dim)])
        trial_value = f(p_trial)
        # compiling results from plot
        if make_plot:
            all_trials_x[i_iter] = p_trial[0]
            all_trials_y[i_iter] = p_trial[1]
            all_results[i_iter] = trial_value
        #if trial values is better than best position, this gets substituted
        #Do with changing in place
        if trial_value < best_value:
            best_position = np.copy(p_trial)
            best_value  = trial_value
        else:
            #check whether it's time to set radius to smaller one. Resets failcount
            fail_count += 1
        if fail_count == reduce_iter:
            radius *= reduce_frac
            fail_count = 0
    # plotting
    if make_plot:
        return best_value, best_position, all_results
	else:
		return best_value, best_position
