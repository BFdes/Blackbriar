import numpy as np
import random as rnd
from optimization_utilities import LS_f_v2 as LS_f
from optimization_utilities import LS_p_v2 as LS_p
#This version of the function is not vectorized. Explicitly does NOT use numpy facilites
def LS_v3(f, p_init, max_iter, bounds, radius, reduce_iter, reduce_frac, params=False):
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
    # plotting utilities
    make_plot = params
    if dim < 1 and make_plot:
        print("warning, only 1 dimension, cannot plot")
    
    # if we are plotting then we use
    if make_plot:
        # creating arrays for the plots
        return LS_p(f, p_init, max_iter, bounds, radius,
                    reduce_iter, reduce_frac)
    # if we are not collecting results for plotting
    else:    
        #search loop
        return LS_f(f, p_init, max_iter, bounds, radius, 
                    reduce_iter, reduce_frac)
