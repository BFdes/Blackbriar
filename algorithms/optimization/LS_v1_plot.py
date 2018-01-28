import numpy as np
import random as rnd
import matplotlib.pyplot as plt
#This version of the function is not vectorized. Explicitly does NOT use numpy facilites
def LS_v1(f, p_init, max_iter, bounds, radius, reduce_iter, reduce_frac, params = False):
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

    this algorithm uses lists and not numpy arrays

    '''
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
        all_trials_x = [0 for iD in range(max_iter)]  
        all_trials_y = [0 for iD in range(max_iter)]  
        all_results = [0 for iD in range(max_iter)] 
    #search loop
    for i_iter in range(0,max_iter):
        print('best_value = ',best_value,'   radius = ',radius)
        # tries random values in the vecinity of the best position so far
        p_trial = [best_position[iD] + radius * random.uniform(bounds[iD][0],bounds[iD][1])  for iD in range(dim)]
        trial_value = f(p_trial)
        # compiling results from plot
        if make_plot:
            all_trials_x[i_iter] = p_trial[0]
            all_trials_y[i_iter] = p_trial[1]
            all_results[i_iter] = trial_value 
        #if trial values is better than best position, this gets substituted
        #Do with changing in place
        if trial_value < best_value:
            best_position = p_trial[:] 
            best_value  = trial_value
        else:
            fail_count += 1
        #check whether it's time to set radius to smaller one.
        if fail_count == reduce_iter:
            radius *= reduce_frac
            fail_count = 0
            
    # plotting 
  
    if make_plot:
        plt.scatter(all_trials_x, all_trials_y, marker=".", c=all_results, cmap="seismic")
        #plot(all_trials[1, :], all_trials[2, :], "o")#, p_new[2])
        plt.show()
  
    return best_value, best_position