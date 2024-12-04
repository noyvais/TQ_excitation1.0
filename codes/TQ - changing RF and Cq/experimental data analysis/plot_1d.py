import os
import numpy
import math
import cmath
import matplotlib.pyplot as plt
numpy.set_printoptions(threshold=numpy.inf)

leftppm=649.51
rightppm=-622.21
size=8192
leftkHz=51
rightkHz=-48.8

data_static = numpy.loadtxt('Zeolites-static.txt',skiprows=3016, max_rows=2192)
data_mas = numpy.loadtxt('Zeolites-mas.txt',skiprows=3010, max_rows=2192)
data_mas = 1.2*data_mas
#data = 2.*(a - numpy.min(a))/numpy.ptp(a)-1 # normalization between 1 and -1
x = numpy.linspace(leftkHz, rightkHz, size) #the grid to which the x data corresponds
x = x[3000:-3000]
nx = x.shape[0]
print(nx)
step_x = 320 # step between consecutive labels
x_positions = numpy.arange(0,nx,step_x) # pixel count at label position
x_labels = [16,12,8,4,0,-4,-8]
plt.plot(data_mas, label='MAS')
plt.plot(data_static, label='Static')
plt.xticks(x_positions, x_labels)
plt.yticks([])  
plt.legend(loc="upper left")
plt.xlabel("Chemical Shift [kHz]")
plt.annotate('*', xy=(535, 1.8e4), xytext=(535, 8e4), size=16, 
            arrowprops=dict(arrowstyle='->'), ha='center')
plt.savefig("mas-static.png", dpi=300)
plt.show()