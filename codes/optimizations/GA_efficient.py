import numpy as np
import sys
import os
import math
import time
import threading 

# parameters for NMR simulations 
io_prefix = "quad_test"
baseline = open("baseline.txt", "r").read().split(",")
var_baselines = [baseline[i] for i in range(len(baseline))]
var_lines = [21,22,23,24,18,19,20]
norm = 1

# parameters for gradient ascent
variable_ranges = [(0, 8), (0,8), (0,8), (0,8), (0,100), (0,100), (0,100)] 
epsilon = [0.05, 0.05, 0.05, 0.05, 5., 5., 5.]
learning_rates = np.array([1., 1., 1., 1., 1000., 1000., 1000.])
n_startpoints = 2
max_iter = [250]*n_startpoints
tolerance = 1e-6
beta1=0.75
beta2=0.95
decay_factor=0.99

# parameters for threading
threads = []
optimized_point = [None]*n_startpoints
optimized_value = [0]*n_startpoints

# replace parameters in simulations
def replacement(lineNum, content, index):
  data = open(f"{io_prefix}{index}.in", 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  with open(f"{io_prefix}{index}.in", 'w') as fileq:
    fileq.writelines(data)

# function to optimize: NMR signal
def nmr_signal(x, index):
  for i in range(x.shape[0]):
    if (x[i]<0):
      x[i]=0
    replacement(var_lines[i], var_baselines[i] + str(x[i]), index)
  os.system(f"simpson {io_prefix}{index}.in")
  return (math.sqrt((np.loadtxt(f"{io_prefix}{index}.fid",usecols=(1)))**2+((np.loadtxt(f"{io_prefix}{index}.fid",usecols=(2)))**2)))/norm 
    
# approximation of the gradient, calculating central difference to make the estimation more accurate
def compute_gradient(func, point, index):
    print(f"thread n  {index} is running")
    gradient = np.zeros_like(point)
    for i in range(len(point)):
        point_p = point.copy()
        point_m = point.copy()
        point_p[i] += epsilon[i]
        point_m[i] -= epsilon[i]
        gradient[i] = (func(point_p, index)-func(point_m, index))/(2*epsilon[i])
    print(f"gradient is {gradient}")
    return gradient

def gradient_ascent(func, initial_point, max_iter, tolerance, learning_rate, index):
    global epsilon, beta1, beta2, decay_factor
    p = np.array(initial_point, dtype=float)
    m = np.zeros_like(initial_point)  
    v = np.zeros_like(initial_point) 
    t=0
    for iteration in range(max_iter[index]):
        p_new = np.zeros_like(initial_point)
        t+=1
        gradient = compute_gradient(func, p, index)
        m = beta1*m+(1-beta1)*gradient
        v = beta2*v+(1-beta2)*gradient**2
        m_hat = m/(1-beta1**t)
        v_hat = v/(1-beta2**t)
        for i in range(len(variable_ranges)):
          p_new[i] = p[i] + learning_rate[i]*m_hat[i]/(np.sqrt(v_hat[i])+epsilon[i])
          if np.abs(gradient[i]) < 1e-3:
            print("tiny gradient")
        print(f"next point is {p_new}  and the function value is {func(p_new, index)}")
        print(f"last point was {p} and the function value was {func(p, index)}")
        if np.abs(func(p, index)) < tolerance: # if we accidently converged to zero signal
          p = np.array([float(int(np.random.uniform(low, high))) for low, high in variable_ranges])
          print("new random point is", p)
          gradient = compute_gradient(func, p, index)
          m = beta1*m+(1-beta1)*gradient
          v = beta2*v+(1-beta2)*gradient**2
          m_hat = m/(1-beta1**t)
          v_hat = v/(1-beta2**t)
          for i in range(len(variable_ranges)):
            if np.abs(gradient[i]) < 1e-3:
              p_new[i] = p[i] + learning_rate[i]*m_hat[i]/(np.sqrt(v_hat[i])+epsilon[i])
              learning_rate[i] *= 1.1
              print("tiny gradient")
            else:
              p_new[i] = p[i] + learning_rate[i]*m_hat[i]/(np.sqrt(v_hat[i])+epsilon[i])
              learning_rate[i] *= decay_factor
        
        # test for convergence
        if np.abs(func(p_new, index) - func(p, index)) < tolerance and np.all(np.abs(gradient) < 8e-3):
            print(f"Converged at iteration {iteration}")
            break
        p = p_new
    print(f"point is: {p}")
    print(f" and value is {func(p, index)}")
    return p, func(p, index)
    
def thread_task(func, initial_point, max_iter, tolerance, learning_rates, i):
  optimized_point[i], optimized_value[i] = gradient_ascent(func, initial_point, max_iter, tolerance, learning_rates, i) 

# Function to perform gradient ascent from multiple random starting points
def optimize_from_random_starts(func, variable_ranges, num_random_starts, max_iter, tolerance, learning_rates, data):
    for i in range(n_startpoints):
        # create copy of input file with star tpoint index and put the data into it
        with open(f"{io_prefix}{i}.in", 'w') as file_i:
          file_i.writelines(data)
        initial_point = np.array([float(int(np.random.uniform(low, high))) for low, high in variable_ranges])
        print(f"init point is {initial_point}")
        thread = threading.Thread(target=thread_task, args=(func, initial_point, max_iter, tolerance, learning_rates, i))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
      thread.join()
       
    opt_value = max(optimized_value)
    opt_index = optimized_value.index(opt_value)
    opt_x = optimized_point[opt_index]
    end = time.time()
    print(f"Total runtime of the program is {end - start}") 
    return opt_x, opt_value
    
start = time.time()
# get data from quad_test.in to duplicate 
data = open(f"{io_prefix}.in", 'r').readlines()
optimized_point, max_value = optimize_from_random_starts(nmr_signal, variable_ranges, n_startpoints, max_iter, tolerance, learning_rates, data)
print(f"Optimized point: {optimized_point}")
print(f"Function value at optimized point: {max_value}")
