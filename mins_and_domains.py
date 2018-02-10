def opt_domains(DIM):

    domains = dict{"sphere_sum":(-5.12,5.12),"difpow_sum":(-1,1),
    "hypEll": (-65.536,65.536),"ackley":(-32.768,-32.768),"griewank":(-600,600),
    "schwefel":(-500,500),"zakharov":(-5,10), "dixon_price":(-10,10),
    "rosenbrock":(-5,10),"rastrigin":(-5.12,5.12),"styTang"=(-5,5),
    "levy":(-10,10), "trid": (-DIM**2,DIM**2), "stepint":(-5.12,5.12),"stepS":(-5.12,5.12)}
    #Fixed for the moment, but some solutions will require the number of dimensions
    #Might also be interesting to add the global minimum coordinates, would
    #require the same


    return domains

def opt_minimums(DIM):
    minimums = dict{"sphere_sum":0,"difpow_sum":0,"hypEll": 0,"ackley":0,"griewank":0,
    "schwefel":0,"zakharov":0, "dixon_price":0,"rosenbrock":0,"rastrigin":0,
    "styTang":=-39.16599*DIM, "levy":0, "trid": -DIM*(DIM+4)*(DIM-1)/6, "stepint",:0,"stepS":0}
    return minimums
