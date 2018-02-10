import numpy as np
import random

'''
Functions that will be optimized, from website at
Surjanovic, S. & Bingham, D. (2013). Virtual Library of Simulation Experiments:
Test Functions and Datasets.
Retrieved January 17, 2018, from http://www.sfu.ca/~ssurjano.
I'm vectorizing them right now
'''

domains = dict{"sphere_sum":(-5.12,5.12),"difpow_sum":(-1,1),
"hypEll": (-65.536,65.536),"ackley":(-32.768,-32.768),"griewank":(-600,600),
"schwefel":(-500,500),"zakharov":(-5,10), "dixon_price":(-10,10),
"rosenbrock":(-5,10),"rastrigin":(-5.12,5.12),"styTang"=(-5,5),
"levy":(-10,10), "trid": (-DIM**2,DIM**2), "stepint":(-5.12,5.12),"stepS":(-5.12,5.12)}
#Fixed for the moment, but some solutions will require the number of dimensions
#Might also be interesting to add the global minimum coordinates, would
#require the same
minimums = dict{"sphere_sum":0,"difpow_sum":0,"hypEll": 0,"ackley":0,"griewank":0,
"schwefel":0,"zakharov":0, "dixon_price":0,"rosenbrock":0,"rastrigin":0,
"styTang":=-39.16599*DIM, "levy":0, "trid": -200, "stepint",:0,"stepS":0}

#sphere function. Minimum at 0
#domain is [-5.12,5.12] at f=0
def sphere_sum(dimension, variables):
    return np.sum(variables)

#sum of different squares function. One global minimum
#domain is [-1,1]. Minimum is at f=0 for all 0
#must be indexed at 1, that's why we add 1
def difpow_sum(dimension, variables):
    return np.sum(np.power(np.abs(variables),range(1,dimension+1)))

#the hyper ellissoid function
#domain is [-65.536,65.536], minimum is at 0 with all 0s
def hypEll(dimension, variables):
#TODO
    return np.sum(np.power(variables,2))

#Ackley function, n dimensional with many local minima and one global minimum
#domain is [-32.768,-32.768], minimum is 0 at all 0s. Using recommended parameters from websit
def ackley(dimension, variables):
    a=20.0
    b=0.2
    c=2*np.pi
    e=-a*np.exp(-b*np.sqrt((1/float(dimension))*np.sum(np.power(variables,2))))
    f=np.exp((1/float(dimension))*np.sum(np.cos(c*variables)))
    return e+f+a+np.exp(1.0)

#The Griewank function, n dimensional with many distributed local minima
#domain is [-600,600] for all. Minimum at f=0 f. Indexed at 1!
def griewank(dimension, variables):
    a=np.sum(np.power(variables,2))/4000.0
    b=np.prod(np.cos(np.divide(variables,np.sqrt(range(1,dimension+1)))))
    return  a - b +1


#the Schwefel function
#domain is [-500,500]. minimum at f=0 for all x=420.9687
def schwefel(dimension, variables):
    a=sum(np.multiply(variables,np.sin(np.sqrt(np.abs(variables)))))
    return 418.9829*dimension -a

#the zakharov function. Quite plain, one global minima and no local
#domain is [-5,10], minimum is f=0 at all 0
def zakharov(dimension, variables):
    a=np.sum(np.power(variables,2))
    b=np.sum(0.5*np.multiply(range(1,dimension+1),variables))**2
    c=b**2
    return a+b+c

##Three hump camel function. Actually works in only 2 dimensions, 3 local minima
#domain is [-5,5]. Minimum at f=0 for 0,0
#TODO, VECTORIZE
def three_hump_camel(dimension, variables):
    return (2.0*variables[0]**2) -(1.05*variables[1]**4) +((1.0/6.0)*variables[0]**6)+variables[0]*variables[1]+variables[1]**2

#Dixon-Price function.
#domain is [-10,10]. Minimum at f=0 for complex expression, with x[i]=2**((-2**i-2)/(2**i))
def dixon_price(dimension, variables):
    a=(variables[0]-1)**2
    b=np.sum(np.multiply(range(2,dimension+1),np.power(2*variables[1:]-variables[:dimension],2)))
    return a+b
#Rosenbrock function
#domain is [-5,10] but reduced here to [-2.048, 2.048], minimum is f=0 at all 1
def rosenbrock(dimension,variables):
    return np.sum(100*np.power(variables[1:]-variables[:dimension],2)+np.power(variables[:dimension]-1,2))
#rastrigin function
#domain is [-5.12,5.12], minimum is f=0 for all 0
def rastrigin(dimension, variables):
    return 10*dimension+np.sum(np.power(variables,2)-10*np.cos(2*np.pi*variables))
#TODO, vectorize this one too
'''
#powell function
#domain is [-4, 5], minimum at f = 0 for all 0
def powell(dimension, variables):
    return sum( for i in xrange(1,dimension/4))
'''
#stiblynsky tang function
#[-5, 5] with minimum f=-39.16599*dimension at x= -2.903534
def styTang(dimension, variables):
    return 0.5*np.sum(np.power(variables,4)-16*np.power(variables,2)+5*variables)
#generalized penalized function from Tu and Lu 2004
#domain [-50,50]. Minimum is at all x = -1. For u the values are 10, 100, 4
def genPenal(dimension,variables):
#TODO
    a=math.cos(math.pi*1.0+0.25*(variables[1]+1))**2
    b=sum((((1.0+0.25*(variables[i]+1)-1)**2)*(1+10*math.sin(math.pi*1.0+0.25*(variables[i+1]+1)))) for i in xrange(1,dimension))
    c=(1.0+0.25*(variables[dimension]+1)-1)**2
    u=[0]*(dimension)
    for j in xrange(1,dimension+1):
        if variables[j]>10:
            u[j-1]=100*(variables[j]-10)**4
        elif (variables[j] > -10 and variables[j]<10):
            u[j-1]=0
        else:
            u[j-1]=100*(-variables[j]-10)**4
    d=sum(u[i] for i in xrange(0,dimension))
    return (math.pi/float(dimension))*(a+b+c)+d
#Levy function.
#domain is [-10,10], Minimum is at all x=1 for f=0
def levy(dimension, variables):
    varW=1+(variables-1)/4
    a=np.sin(np.pi*varW[0])**2
    b1=np.power(var[:dimension-1]-1,2)
    b2=1+np.power(np.sin(np.pi*varW[:dimension-1]+1),2)
    b=np.sum(np.multiply(b1,b2))
    c1=np.power(var[dimension-1]-1,2)
    c2=1+np.power(np.sin(2*np.pi*varW[dimension-1]),2)
    c=np.multiply(c1,c2)
    return a+b+c

#changing global minimum. Might be best to evaluate for d=10
#[-d**2,d**2] bat d 10 it's f=-200
def trid(dimension, variables):
    a=np.sum(np.power(variables-1,2))
    b=np.sum(np.multiply(variables[1:],variables[:dimension-1]))
    return a+b

#simple integer step,
#domain is [-5.12,5.12], Minimum is at all x=0 for f=0
def stepint(dimension, variables):
    return 25.0+np.sum(np.floor(variables))
#a discretization of the sphere function
#domain is [-5.12,5.12] at f=0
def stepS(dimension, variables):
    return np.sum(np.power(np.floor(variables+0.5),2))
#quartic function
#domain is very small [-1.28,1.28] with minima at all 0 for f=<15, yes there is no precise minimum
def quartic(dimension, variables):
    a=np.sum(np.multiply(range(1,dimension+1),np.power(variables,4)))
    b=0.5#np.random.uniform(0,1)
    return a+b
#the beale function is only in 2 dimensions
#the domain is between [-4.5,4.5] with the minimum at f=0 with x = 3 and 0.5
def beale(dimension, variables):
    a=(1.5-variables[1]+variables[1]*variables[2])**2
    b=(2.25-variables[1]+variables[1]*(variables[2]**2))**2
    c=(2.625-variables[1]+variables[1]*(variables[2]**3))**2
    return a+b+c
#the easom function, only 2 dimension
#domain is [-100,100] with f=-1 at minimum with exes equal to pi
def easom(dimension, variables):
    a=-math.cos(variables[1])*math.cos(variables[2])
    b=math.exp(-(variables[1]-math.pi)**2 - (variables[2]-math.pi)**2)
    return a*b
#the matyas function, also 2 dimensions
#domain is [-10,10] with f=0 at x=0
def matyas(dimension, variables):
    return 0.26*(variables[1]**2 + variables[2]**2)-0.48*variables[1]*variables[2]

#The eggholder function, 2 dimensions and many local minima
#domain is [-512,512]. Minimum at f=-959.6407 for 512,404.2319

def eggholder(dimension, variables):
    a=math.sin(math.sqrt(abs(variables[2]+ (variables[1]/2.0) +47)))
    b=math.sin(math.sqrt(abs(variables[1]-(variables[2] +47))))
    return -(variables[2]+47)*a -variables[1]*b
