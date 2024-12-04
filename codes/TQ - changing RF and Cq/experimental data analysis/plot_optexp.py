import os
import numpy
import math
import cmath
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
numpy.set_printoptions(threshold=numpy.inf)

# 10 rows of headers
# ignore final row
# read as complex directly
par1_size = 12
par2_size = 12
size = 102960
nperpar = int((size/(par2_size*par1_size))/1)
first = 0
step = 1 #INC of optimization 

if (first):
  replacements = {'i':'j'}
  with open('3p_opt.txt') as infile, open('3popt_updated.txt', 'w') as outfile:
      for line in infile:
        for src, target in replacements.items():
          line = line.replace(src, target)
        outfile.write(line)

a = numpy.loadtxt('2popt_updated.txt',skiprows=10, max_rows=size)
data = a/78000

x_old = numpy.arange(1,par1_size*par2_size+1, step) #the grid to which the x data corresponds
x = numpy.repeat(x_old, nperpar)
nx = x.shape[0] 
step_x = 20*nperpar # step between consecutive labels
print(step_x)
x_positions = numpy.arange(0,nx,step_x) # pixel count at label position
x_labels = x[::step_x] # labels you want to see
plt.ylim(-1, 1)
plt.plot(data)
plt.xticks(x_positions, x_labels)
#plt.title("3pls Optimization")
plt.ylabel("Intensity")
plt.xlabel("Experiment number")
plt.savefig("2p_opt_inset.png", dpi=300)
plt.show()