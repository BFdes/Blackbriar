# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:29:30 2018

@author: AntonioE89
"""
import numpy as np
import random as rnd
#This version of the function is not vectorized. Explicitly does NOT use numpy facilites
def RS_v1(f, p_best, max_iter, bounds, params=False):
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

    '''
    #initialization
    best_position = p_best
    best_value = f(p_best)
    dim = len(p_best)
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
        print('best_value = ',best_value)
        # tries random values in the vecinity of the best position so far
        p_trial = np.array([rnd.uniform(bounds[i][0],bounds[i][1]) for i in range(dim)])
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
    # plotting
    if make_plot:
        return best_value, best_position, all_results
    else:
        return best_value, best_position