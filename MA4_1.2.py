import random
import math
import functools
import concurrent.futures as future
from time import perf_counter as pc

def approximate_hypersphere_volume(n, d, i = None):
    r = 1 # Set r = 1 to be constant

    n_hypersphere = 0
    n_hypercube = n
    V_hypercube = (2*r)**d

    for _ in range(n):
        rand_nums = [random.uniform(-r, r)**2 for _ in range(d)] # List comprehension
        norm = functools.reduce(lambda x,y: x+y, rand_nums) # Reduce and lambda
        if norm <= 1:
            n_hypersphere += 1

    

    # As n_hypersphere / n_hypercube = V_hypersphere / V_hypercube, we have
    V_hypersphere = n_hypersphere / n_hypercube * V_hypercube

    V_hypersphere_formula = lambda d: math.pi**(d/2) / math.gamma(d/2 + 1) # Lambda

    print("\n----------------------")
    print(f"Number of points: {n}")
    print(f"Number of dimensions: {d}")
    print(f"Number of points in hypersphere: {n_hypersphere}")
    print(f"Approximation of hypersphere volume: {V_hypersphere}")
    print(f"Exact value of V_d(1): {V_hypersphere_formula(d)}")
    print("----------------------")

def main():
    for conf in [(100000, 2), (100000, 11)]:
        approximate_hypersphere_volume(conf[0], conf[1])


    print("\n----------------------")
    print("Timings:")
    
    print("Timing no multiprocessing")
    start = pc()
    approximate_hypersphere_volume(10000000, 11)
    end = pc()
    time_no_multiprocessing = round(end-start, 2)
    print(f"Time no multiprocessing: {time_no_multiprocessing} s")

    print("Timing multiprocessing")
    start = pc()

    with future.ProcessPoolExecutor() as ex: 
        iterations = range(10)
        results = ex.map(approximate_hypersphere_volume(1000000, 11), iterations)
        
    end = pc()
    time_multiprocessing = round(end-start, 2)
    print(f"Time multiprocessing: {time_multiprocessing} s")
        
    print("\n----------------------")

if __name__ == "__main__":
    main()

# 1.2:
# ----------------------
# Number of points: 100000
# Number of dimensions: 2
# Number of points in hypersphere: 78556
# Approximation of hypersphere volume: 3.14224
# Exact value of V_d(1): 3.141592653589793
# ----------------------

# ----------------------
# Number of points: 100000
# Number of dimensions: 11
# Number of points in hypersphere: 90
# Approximation of hypersphere volume: 1.8432
# Exact value of V_d(1): 1.8841038793898994
# ----------------------


# 1.3:
# Time no multiprocessing: 50.8 s
# Time multiprocessing: 5.09 s
# About a 10 time difference was seen in the  multiprocessing when compared
# not using multiprocessing. This is due to the fact that the program
# is running in 10 separate processes in parallell with 10 times as few
# amount of points.