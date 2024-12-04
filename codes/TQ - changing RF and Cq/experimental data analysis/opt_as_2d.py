import os
import numpy
import math
import cmath
import matplotlib.pyplot as plt
numpy.set_printoptions(threshold=numpy.inf)

# 10 rows of headers
# ignore final row
# read as complex directly
par1_size = 7
par2_size = 7
nperpar = 715
size = 35036
first = 1
minpar1 = 2 #lowest value of par1- for plotting
minpar2 = 2 #lowest value of par2- for plotting
maxpar1 = 8 #lowest value of par1- for plotting
maxpar2 = 8 #lowest value of par2- for plotting
step_par1 = 1 #INC of optimization par1- for plotting
step_par2 = 1 #INC of optimization par2- for plotting

if (first):
  replacements = {'i':'j'}
  with open('2pls_opt.txt') as infile, open('2pls_updated.txt', 'w') as outfile:
      for line in infile:
        for src, target in replacements.items():
          line = line.replace(src, target)
        outfile.write(line)

data = numpy.loadtxt('2pls_updated.txt',skiprows=10, max_rows=size-1, dtype=numpy.complex128)
data_3d = numpy.reshape(data, (par2_size, par1_size, nperpar))

intensities = numpy.zeros((par2_size, par1_size))
for col in range(data_3d.shape[0]):
  for row in range(data_3d.shape[0]):
    intensities[col, row] = numpy.max(numpy.abs(numpy.real(data_3d[col, row,:])))

x = numpy.arange(minpar1, maxpar1+step_par1, step_par1) #the grid to which the x data corresponds
nx = x.shape[0] # = par1_size
step_x = 1 # step between consecutive labels
x_positions = numpy.arange(0,nx,step_x) # pixel count at label position
x_labels = x[::step_x] # labels you want to see
y = numpy.arange(minpar2, maxpar2+step_par2, step_par2) #the grid to which the y data corresponds
ny = y.shape[0] # = par2_size
step_y = 1
y_positions = numpy.arange(0,ny,step_y) 
y_labels = y[::step_y]
plt.xticks(x_positions, x_labels)
plt.yticks(y_positions, y_labels)
plt.imshow(intensities)  
plt.colorbar()
plt.title("Signal After TQ Evolution \n Using a 2 Pulse Scheme")
plt.ylabel("First Pulse Duration")
plt.xlabel("Second Pulse Duration")
plt.savefig("2plS_opt.png", dpi=300)
plt.show()