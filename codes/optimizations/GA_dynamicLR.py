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
var_lines = [21,22,23,24,18,19,20]#,15]
norm = 1

# parameters for gradient ascent
variable_ranges = [(0, 8), (0,8), (0,8), (0,8), (0,100), (0,100), (0,100)]#, (500,50000)] 
epsilon = [0.05, 0.05, 0.05, 0.05, 5., 5., 5.]#, 5000.]
learning_rates = np.array([1., 1., 1., 1., 1000., 1000., 1000.])#, 1e10])
n_startpoints = 10
max_iter = 250
tolerance = 1e-6
beta1=0.9
beta2=0.999
decay_factor=0.99

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
        point_p[i] += epsilon[i]
        point_m[i] -= epsilon[i]
        gradient[i] = (func(point_p)-func(point_m))/(2*epsilon[i])
    print(f"gradient is {gradient}")
    return gradient

def gradient_ascent(func, initial_point, max_iter, tolerance, learning_rate):
    global epsilon, beta1, beta2, decay_factor
    p = np.array(initial_point, dtype=float)
    m = np.zeros_like(initial_point)  # First moment estimate
    v = np.zeros_like(initial_point)  # Second moment estimate
    t=0
    for iteration in range(max_iter):
        p_new = np.zeros_like(initial_point)
        t+=1
        gradient = compute_gradient(func, p)
        m = beta1*m+(1-beta1)*gradient
        v = beta2*v+(1-beta2)*gradient**2
        m_hat = m/(1-beta1**t)
        v_hat = v/(1-beta2**t)
        for i in range(len(variable_ranges)):
          p_new[i] = p[i] + learning_rate[i]*m_hat[i]/(np.sqrt(v_hat[i])+epsilon[i])
          if np.abs(gradient[i]) < 1e-5:
            #learning_rate[i] *= 1.01
            print("tiny gradient")
          elif np.abs(gradient[i]) > 1e-1:
            print("big gradient")
            #learning_rate[i] *= decay_factor
        print(f"next point is {p_new}  and the function value is {func(p_new)}")
        print(f"last point was {p} and the function value was {func(p)}")
        if np.abs(func(p)) < tolerance or any(p[i] > variable_ranges[i][1]+0.1*variable_ranges[i][1] for i in range(len(p))): # if we accidently converged to zero signal OR surpassed the upper limit of a variable
          p = np.array([float(int(np.random.uniform(low, high))) for low, high in variable_ranges])
          print("new random point is", p)
          gradient = compute_gradient(func, p)
          m = beta1*m+(1-beta1)*gradient
          v = beta2*v+(1-beta2)*gradient**2
          m_hat = m/(1-beta1**t)
          v_hat = v/(1-beta2**t)
          for i in range(len(variable_ranges)):
            if np.abs(gradient[i]) < 5e-5:
              p_new[i] = p[i] + learning_rate[i]*m_hat[i]/(np.sqrt(v_hat[i])+epsilon[i])
              #learning_rate[i] *= 1.01
              print("tiny gradient")
            elif np.abs(gradient[i]) > 5e-1:
              p_new[i] = p[i] + learning_rate[i]*m_hat[i]/(np.sqrt(v_hat[i])+epsilon[i])
              print("big gradient")
              #learning_rate[i] *= decay_factor
        
        # test for convergence
        #if np.all(np.abs(gradient) < tolerance):
        if np.abs(func(p_new) - func(p)) < tolerance and np.all(np.abs(gradient) < 8e-3):
            print(f"Converged at iteration {iteration}")
            break
        p = p_new
    print("point is: ", p)
    print(" and value is ", func(p))
    return p, func(p)

# Function to perform gradient ascent from multiple random starting points
def optimize_from_random_starts(func, variable_ranges, num_random_starts, max_iter, tolerance, learning_rates):
    opt_x = None
    opt_value = 0  # starting with zero because we maximize absolute value
    print()
    for i in range(n_startpoints):
        initial_point = np.array([float(int(np.random.uniform(low, high))) for low, high in variable_ranges])
        print("init point is ", initial_point)
        optimized_point, optimized_value = gradient_ascent(func, initial_point, max_iter, tolerance, learning_rates)
        if optimized_value > opt_value:
            opt_value = optimized_value
            opt_x = optimized_point
    end = time.time()
    print(f"Total runtime of the program is {end - start}") 
    with open("results-new.txt", 'w+') as file_i:
          file_i.write("\n")
          file_i.write(f"{opt_x}")
          file_i.write(f"{opt_value}")
    return opt_x, opt_value
    
start = time.time() 
optimized_point, max_value = optimize_from_random_starts(nmr_signal, variable_ranges, n_startpoints, max_iter, tolerance, learning_rates)
print(f"Optimized point: {optimized_point}")
print(f"Function value at optimized point: {max_value}")
