# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:50:06 2018

@author: AntonioE89
"""
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
#This version of the function is not vectorized. Explicitly does NOT use numpy facilites
def GLS_v2(f, p_init=False, max_iter, bounds, radius, reduce_iter, reduce_frac, params=False, LS_RS_frac):
    '''
    ---------------------
    Generalized Local Seach Algorithm
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
    LS_RS_frac: fraction of total iterations used for LS

    --- Notes ---

    1. This algorithm uses numpy arrays and tries to take advantage of vectorization.
    2. Make_plot decides whether to output all function evaluations
		or not.

    '''
    
    # plotting utilities
    make_plot = params
    if dim < 1 and make_plot:
        print("warning, only 1 dimension, cannot plot")
    #initialization (RS algorithm)
    # determine initial point if not given
    if p_init == False:
        p_init = np.array([rnd.uniform(bounds[i][0],bounds[i][1]) for i in range(dim)])
        
    if make_plot:
        # RS algorithm
        best_value, best_position, all_results = RS_v2(f, p_best, int(max_iter*(1-LS_RS_frac)), 
                                                       bounds, make_plot)
        # LS algorithm
        best_value, best_position, all_results_LS = LS_v2(f, best_position, int(max_iter*LS_RS_frac),
                                                          bounds, radius, reduce_iter, reduce_frac, make_plot)
        # append lists for plorring
        all_results += all_results_LS
        return best_value, best_position, all_results
    
    else:
        # RS algorithm
        best_value, best_position = RS_v2(f, p_best, int(max_iter*(1-LS_RS_frac)), 
                                          bounds, make_plot)
        # LS algorithm
        best_value, best_position = LS_v2(f, best_position, int(max_iter*LS_RS_frac),
                                          bounds, radius, reduce_iter, reduce_frac, make_plot)
        return best_value, best_position

        
