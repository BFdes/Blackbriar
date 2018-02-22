import numpy as np
import random as rnd
'''
This utility file has all sub-blocks for building optimization algorithms   
'''
def LS_f_v2(f, p_init, max_iter, bounds, radius, reduce_iter, reduce_frac):
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
    3. f stands for "fast implementation" which means it does not compile results    

    '''
    #initialization
    best_position = p_init
    best_value = f(p_init)
    dim = len(p_init)
    fail_count = 0
    # plotting utilities
    for i_iter in range(max_iter):
        # tries random values in the vecinity of the best position so far
        p_trial = best_position + radius * np.array(
                [rnd.uniform(bounds[i][0],bounds[i][1]) for i in range(dim)])
        trial_value = f(p_trial)
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
    return best_value, best_position

def LS_p_v2(f, p_init, max_iter, bounds, radius, reduce_iter, reduce_frac):
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
    3. p stands for "plotting" which means it compiles results that you can later plot

    '''
    #initialization
    best_position = p_init
    best_value = f(p_init)
    dim = len(p_init)
    fail_count = 0
    # lists for compiling results
    all_trials_x = np.zeros(max_iter)
    all_trials_y = np.zeros(max_iter)
    all_results = np.zeros(max_iter)
    for i_iter in range(max_iter):
        # tries random values in the vecinity of the best position so far
        p_trial = best_position + radius * np.array([rnd.uniform(bounds[i][0],bounds[i][1]) for i in range(dim)])
        trial_value = f(p_trial)
        # compiling results from plot
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
    return best_value, best_position, all_results

def RS_f_v1(f, p_best, max_iter, bounds):
    '''
    ---------------------
    Random Seach Algorithm
    ---------------------

    --- input ---

    f: objective function
    p_best: hot-start a best point
    max_iter: maximum number of iterations
    bounds: bounds on the search domain

    --- Notes ---

    1. p_best is used in case a good value is already known.
    2. f stands for "fast implementation" which means it does not compile results

    '''
    #initialization
    best_position = p_best
    best_value = f(p_best)
    dim = len(p_best)
    #search loop
    for i_iter in range(max_iter):
        print('best_value = ',best_value)
        # tries random values in the vecinity of the best position so far
        p_trial = np.array([rnd.uniform(bounds[i][0],bounds[i][1]) for i in range(dim)])
        trial_value = f(p_trial)
        #if trial values is better than best position, this gets substituted
        #Do with changing in place
        if trial_value < best_value:
            best_position = np.copy(p_trial)
            best_value  = trial_value
    return best_value, best_position

def RS_p_v1(f, p_best, max_iter, bounds):
    '''
    ---------------------
    Random Seach Algorithm
    ---------------------

    --- input ---

    f: objective function
    p_best: hot-start a best point
    max_iter: maximum number of iterations
    bounds: bounds on the search domain

    --- Notes ---

    1. p_best is used in case a good value is already known.
    2. p stands for "plotting" which means it compiles results that you can later plot

    '''
    #initialization
    best_position = p_best
    best_value = f(p_best)
    dim = len(p_best)
    # creating arrays for the plots
    all_trials_x = np.zeros(max_iter)
    all_trials_y = np.zeros(max_iter)
    all_results = np.zeros(max_iter)
    #search loop
    for i_iter in range(max_iter):
        print('best_value = ',best_value)
        # tries random values in the vecinity of the best position so far
        p_trial = np.array([rnd.uniform(bounds[i][0],bounds[i][1]) for i in range(dim)])
        trial_value = f(p_trial)
        # compiling results from plot
        all_trials_x[i_iter] = p_trial[0]
        all_trials_y[i_iter] = p_trial[1]
        all_results[i_iter] = trial_value
        #if trial values is better than best position, this gets substituted
        #Do with changing in place
        if trial_value < best_value:
            best_position = np.copy(p_trial)
            best_value  = trial_value
    return best_value, best_position, all_results
    
    
    
    
    
    
