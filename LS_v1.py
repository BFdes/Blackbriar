import math
import random

#This version of the function is not vectorized. Explicitly does NOT use numpy facilites
def function LS_v1(f, p_init, max_iter, bounds, radius, reduce_iter, reduce_frac; params=[false]):
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
	#initialization
	best_position = p_init
  	best_value = f(p_init)
	dim = len(p_init)
    fail_count = 0
    #search loop
    for i_iter in range(0,max_iter):
        # tries random values in the vecinity of the best position so far
        p_trial = [best_position[iD] + radius * random.uniform(bounds[iD,0],bounds[iD,1])  for iD in range(dim)]
        trial_value = f(p_trial)
        #if trial values is better than best position, this gets substituted
        #Do with changing in place
        if trial_value < best_value:
          	best_position = p_trial 
          	best_value  = trial_value
        else:
          	fail_count += 1
      	#check whether it's time to set radius to smaller one.      if fail_count == reduce_iter:
        	radius *= re duce_frac
            fail_count =   0
  
	return best_value, best_postion



