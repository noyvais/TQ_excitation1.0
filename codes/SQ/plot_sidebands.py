import os
import numpy
import math
import cmath
import matplotlib.pyplot as plt
from pyfonts import load_font
#import logging
#logging.basicConfig(level=logging.DEBUG)
#numpy.set_printoptions(threshold=numpy.inf)
# load font
font = load_font(
   font_url="https://github.com/jondot/dotfiles2/blob/master/.fonts/cambria.ttf?raw=true"
)

i=-1
offs_x=1500
offs_y=400
CQ= numpy.array([10, 15, 20, 25, 50])
R= numpy.array([0.004, 0.009, 0.015, 0.024, 0.034, 0.091])
Z=numpy.array([25,20,15,10,5])

for j in range(len(CQ)):
  i = i+1
  x = numpy.loadtxt('sidebands'+str(CQ[j])+'.spe', usecols=(0))
  y = numpy.loadtxt('sidebands'+str(CQ[j])+'.spe', usecols=(1))
  plt.plot(x+i*offs_x, y+i*offs_y, label='Cq='+str(CQ[j])+'kHz', zorder=Z[j])
  plt.annotate('R='+str(R[j]), xy=(x[0]+i*offs_x, y[0]+35+i*offs_y), fontweight="bold")
  plt.gca().get_yaxis().set_visible(False)
  plt.gca().get_xaxis().set_visible(False)
  
plt.legend(loc="upper right")
fig = plt.gcf()
ax = plt.gca()
fig.set_size_inches(7, 5)
"""
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
"""
plt.savefig("sidebands.png", dpi=300)
plt.show()

