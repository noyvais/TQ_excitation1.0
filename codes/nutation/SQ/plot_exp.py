import os
import numpy
import math
import cmath
import matplotlib.pyplot as plt
numpy.set_printoptions(threshold=numpy.inf)

# 10 rows of headers
# choose number of rows to read
# read as complex directly
p1_size = 200
nperpar = 786
size = 157200
first = 1

minp = 1 #lowest value of p1 for plotting
maxp = 40 #lowest value of p1 for plotting
step_p1 = 1 #INC of optimization 1- for plotting

if (first):
  replacements = {'i':'j'}
  with open('SQ_nutation.txt') as infile, open('SQ_nutation_updated.txt', 'w') as outfile:
      for line in infile:
        for src, target in replacements.items():
          line = line.replace(src, target)
        outfile.write(line)

a = numpy.loadtxt('SQ_nutation_updated.txt',skiprows=10, max_rows=31440)
data = 2.*(a - numpy.min(a))/numpy.ptp(a)-1 # normalization between 1 and -1
x_old = numpy.arange(0, maxp+step_p1, step_p1) #the grid to which the x data corresponds
x = numpy.repeat(x_old, nperpar)
nx = x.shape[0] 
step_x = 5*nperpar # step between consecutive labels
x_positions = numpy.arange(0,nx,step_x) # pixel count at label position
x_labels = x[::step_x] # labels you want to see
plt.plot(data)
print(x.shape)
print(data.shape)
plt.xticks(x_positions, x_labels)
plt.title("SQ nutation")
plt.ylabel("Intensity")
plt.xlabel("Pulse Duration [\u03bcs]")
plt.savefig("sq_nut.png", dpi=300)
plt.show()