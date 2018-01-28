import numpy as np
import random as rnd
#This version of the function is not vectorized. Explicitly does NOT use numpy facilites
def LS_v2(f, p_init, max_iter, bounds, radius, reduce_iter, reduce_frac; params=[False]):
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

this algorithm uses numpy arrays and tries to take advantage of vectorization.
All of them are vectors

'''
	#initialization
	best_position = p_init
  	best_value = f(p_init)
	dim = len(p_init)
    fail_count = 0
    #search loop
    for i_iter in range(max_iter):

        # tries random values in the vecinity of the best position so far        
        p_trial = best_position + radius * nd.array([rnd.uniform(bounds[i][0],bounds[i][1]) for i in range(dim)])
        trial_value = f(p_trial)
        #if trial values is better than best position, this gets substituted
        #Do with changing in place
        if trial_value < best_value:
          	best_position = np.copy(p_trial) 
          	best_value  = trial_value
        else:
            #check whether it's time to set radius to smaller one. Resets failcount
          	fail_count += 1
        	radius *= reduce_frac
            fail_count =   0
  
	return best_value, best_postion



