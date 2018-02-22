# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:29:30 2018

@author: AntonioE89
"""
import numpy as np
import random as rnd
from optimization_utilities import RS_f_v1 as RS_f
from optimization_utilities import RS_p_v1 as RS_p
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
    # plotting utilities
    make_plot = params
    dim = len(p_best)
    if dim < 1 and make_plot:
        print("warning, only 1 dimension, cannot plot")
    # creating arrays for the plots

    if make_plot:
        return RS_p(f, p_best, max_iter, bounds)
    else:
        return RS_f(f, p_best, max_iter, bounds)