'''
---------------------
Computing optimal parameter set
---------------------
In this file we will compute an "optimal" parameter set for each algorithm. This
is done by averaging the performance of parameters for a given algorithm along
many optimization functions for a "small" number of iterations (iterations_op).
Then the "best" parameter set for each algorithm will be stored in a dictionary
to be used in later computations.

Note: there is a clear drawback in this approch in the sense that the parameter
set that can decrease quickly in the first iterations is not necesarly the one
that works best at a later stage of an optimization.
'''
#import utilities
import itertools as itls
import pandas as pd
import json

#create a correct path for all users for personalized scripts
import sys
import os
#taken from http://python.robasworld.com/python-relative-path/
absFilePath = os.path.abspath(__file__)                # Absolute Path of the module. Where we are currently with THIS module
#print(absFilePath)
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module. What is ABOVE this module (e.g. test)
#print(fileDir)
parentDir1 = os.path.dirname(fileDir)                   # Directory of the Module directory. What is ABOVE the previous directory (algorithms)
parentDir2 = os.path.dirname(parentDir1 )                   # Directory of the Module directory. What is ABOVE the previous directory (Blackbriar)

#print(parentDir)

newPath1 = os.path.join(parentDir2, 'algorithms\optimization')   # Get the directory for StringFunctions
newPath2 = os.path.join(parentDir2, 'algorithms\test')   # Get the directory for StringFunctions
newPath3 = os.path.join(parentDir2, 'tests')   # Get the directory for StringFunctions

#print(newPath)

sys.path.append(newPath1)                               # Add path into PYTHONPATH
sys.path.append(newPath2)                               # Add path into PYTHONPATH

#import the solvers
import LS_v1 as LSv1

#import the functions
import optimization_functions as opF
import mins_and_domains as mAd


save_fold='../figures/'
save_json='../dicts/'
names=["sphere_sum","difpow_sum","hypEll","ackley","griewank","schwefel","zakharov","three_hump_camel","dixon_price","rosenbrock",
      "rastrigin","styTang","genPenal","levy","trid","stepint","stepS"]
dimensions = [20, 60] # number of dimension, if more than one, then loop through them

iterations_op=5000

func_dict={
    "sphere_sum": opF.sphere_sum,
    "difpow_sum": opF.difpow_sum,
    "hypEll": opF.hypEll,
    "ackley": opF.ackley,
    "griewank": opF.griewank,
    "schwefel": opF.schwefel,
    "zakharov": opF.zakharov,
    "three_hump_camel": opF.three_hump_camel
    "dixon_price": opF.dixon_price
    "rosenbrock": opF.rosenbrock
    "rastrigin": opF.rastrigin
    "styTang": opF.styTang
    "genPenal": opF.genPenal
    "levy": opF.levy
    "trid": opF.trid
    "stepint": opF.stepint
    "stepS": opF.stepS
}


# here is where we start from
#TODO
#above this we will have the dimension loop.
domains=mAd.domains(dim)
minima=mAd.minimums(dim)
func_bounds=[domains[names] for bound in range(len(names))]
func_counter=0
'''
for name in names: # iterate through every module's attributes
    caller=func_dict[name]
    if callable(caller):                      # check if callable (normally functions)
        loc_name=name
        loc_bounds=func_bounds[func_counter]
        dimension=dimensions[func_counter]
        print 'Using '+loc_name

        #do Bee Swarm
        func_list=[]
        mean_value=[]
        sparrow_ranges = [np.arange(40,70,10),np.arange(0.05,0.19,0.05),np.arange(0.4,0.6,0.1),np.arange(0.3,0.59,0.1),np.arange(2,5,1)]
        #blabla  len(np.arange(0.1,0.6,0.1))*len(np.arange(10,50,10))*len(np.arange(1,4,1))*len(np.arange(10,25,5))*len(np.arange(40,50,5))*len(np.arange(20,35,5))

        #permutations.
        print 'Start Sparrow Swarm'
        dictLocal={}
        par_symb=[]
        #runs through all possible combination of the indicated parameters
        for (j,k,m,n,o) in itls.product(*sparrow_ranges):
            loop_Count_Temp=range(10)
            #execute 10 times the same set of parameters
            for count in loop_Count_Temp:
                #parameters are set in a dictionary
                locDict={
                    'dimension' : dimension,
                    'lBound' : loc_bounds[0],
                    'uBound' : loc_bounds[1],
                    'nSparrows': j,
                    'eliteFrac' : k,
                    'medFrac' : m,
                    'usFrac' : n,
                    'tabuLength' : o,
                    'boxElite' : 5,
                    'boxMedium' : 10,
                    'intIterations' : 10
                }
                #execute the actual search
                func_value=spf.sparrow(iterations_op,locDict,caller)
                #print 'Managed this at iteration', count
                func_list.append(func_value)
                #print func_list
                #print type(func_value)
                #print 'This is the value', func_value
                #print 'counter before', count
            #mean of a set of values
            #print 'Out of the While'
            par_mean=np.median(func_list)
            mean_value.append(par_mean)
            #par_symb.append((i,j))
            #print 'Dict Done for Bee swarm'
            locDict['median']=par_mean
            dictLocal['parSet'+'_'+str(int(len(mean_value)-1))]=locDict
            func_list=[]
            #print 'Finished one set'
        #save parametrs
        #print 'Finished one set'
        best=min(enumerate(mean_value), key=(lambda y: y[1]))
        pass_Dict=dictLocal['parSet'+'_'+str(int(best[0]))]
        with open(save_json+'Sparrow_par_best'+'_'+name+'.json', 'w') as handle:
            json.dump(pass_Dict, handle)
        with open(save_json+'Sparrow_par_list'+'_'+name+'.json', 'w') as handle:
            json.dump(dictLocal, handle)
        print 'Saved stuff for Sparrow Swarm'
        #plot
        light_plot=matplotlib.pyplot.figure(figsize=(12,6))
        plt.title('Mean Function Value',horizontalalignment='center',x=0.5,y=0.9,fontweight='bold',fontsize=15)
        plt.yticks(rotation=90, fontsize=9)
        plt.xlabel('Parameter Set',fontweight='bold', fontsize=12)
        plt.plot(mean_value)
        savefig(save_fold+'Sparrow'+'_'+name+'.png')
        plt.close()
        print 'Function done'

    func_counter+=1
'''
