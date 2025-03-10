import numpy as np
import sys
import os
import math
import time 

# parameters for NMR simulations 
input_file = "quad_test.in"
output_file = "quad_test.fid"
baseline = open("baseline.txt", "r").read().split(",")
var_baselines = [baseline[i] for i in range(len(baseline))]
var_lines = [21,22,23,24,18,19,20]
norm = 1

# parameters for gradient ascent
variable_ranges = [(0, 8), (0, 8), (0, 8), (0, 8), (0, 100), (0, 100), (0, 100)] 
step_sizes = [0.5, 0.5, 0.5, 0.5, 10, 10, 10]
n_startpoints = 20
max_iter = 250
tolerance = 1e-2

# replace parameters in simulations
def replacement(lineNum, content):
  data = open(input_file, 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open(input_file, 'w')
  fileq.writelines(data)

# function to optimize: NMR signal
def nmr_signal(x):
  for i in range(x.shape[0]):
    if (x[i]<0):
      x[i]=0
    replacement(var_lines[i], var_baselines[i] + str(x[i]))
  os.system("simpson quad_test.in")
  return (math.sqrt((np.loadtxt(output_file,usecols=(1)))**2+((np.loadtxt(output_file,usecols=(2)))**2)))/norm 
    
# approximation of the gradient, calculating central difference to make the estimation more accurate
def compute_gradient(func, point):
    gradient = np.zeros_like(point)
    for i in range(len(point)):
        point_p = point.copy()
        point_m = point.copy()
        point_p[i] += step_sizes[i]
        point_m[i] -= step_sizes[i]
        gradient[i] = (func(point_p)-func(point_m))/(2*step_sizes[i])
    return gradient


def gradient_ascent(func, initial_point, max_iter, tolerance):
    global step_sizes
    p = np.array(initial_point, dtype=float)
    for iteration in range(max_iter):
        gradient = compute_gradient(func, p)
        if np.abs(func(p)) < tolerance: # if we accidently converged to zero signal
          p = np.array([float(int(np.random.uniform(low, high))) for low, high in variable_ranges])
          print("new random point is", p)
          gradient = compute_gradient(func, p)
        # perform a step in the direction of the gradient 
        p_new = p+step_sizes*gradient
        
        # test for convergence
        if np.all(np.abs(gradient) < tolerance):
            print(f"Converged at iteration {iteration}")
            break
        p = p_new
    print("point is: ", p)
    print(" and value is ", func(p))
    return p, func(p)

# Function to perform gradient ascent from multiple random starting points
def optimize_from_random_starts(func, variable_ranges, num_random_starts, max_iter, tolerance):
    opt_x = None
    opt_value = 0  # starting with zero because we maximize absolute value
    print()
    for i in range(n_startpoints):
        initial_point = np.array([float(int(np.random.uniform(low, high))) for low, high in variable_ranges])
        print("init point is ", initial_point)
        optimized_point, optimized_value = gradient_ascent(func, initial_point, max_iter, tolerance)
        if optimized_value > opt_value:
            opt_value = optimized_value
            opt_x = optimized_point
    end = time.time()
    print(f"Total runtime of the program is {end - start}") 
    return opt_x, opt_value
    
start = time.time() 
optimized_point, max_value = optimize_from_random_starts(nmr_signal, variable_ranges, n_startpoints, max_iter, tolerance)
print(f"Optimized point: {optimized_point}")
print(f"Function value at optimized point: {max_value}")
