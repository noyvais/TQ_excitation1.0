import os
import numpy
import math
import cmath
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
numpy.set_printoptions(threshold=numpy.inf)
from pyfonts import load_font

font = load_font(
   font_url="https://github.com/jondot/dotfiles2/blob/master/.fonts/cambria.ttf?raw=true"
)

leftppm=100
rightppm=-150
size=2697

data_2p = numpy.loadtxt('2pls-left.txt',skiprows=3220, max_rows=1697)
data_3p = numpy.loadtxt('3pls-left.txt',skiprows=3200, max_rows=1697)
data_4p = numpy.loadtxt('4pls-left.txt',skiprows=3195, max_rows=1697)
norm = numpy.linalg.norm(data_4p, 2)
data_2p = data_2p/norm
data_3p = data_3p/norm
data_4p = data_4p/norm
x_positions = numpy.linspace(100,1597,6)

fig, axes = plt.subplots(3, sharex=True, sharey=True, gridspec_kw = {'wspace':-0.05, 'hspace':0.05})
axes[0].plot(data_2p, label="2pls")
axes[1].plot(data_3p, label="3pls")
axes[2].plot(data_4p, label="4pls")
plt.setp(axes, xticks=x_positions, xticklabels=[135,90,45,0,-45,-90])
axes[0].legend(loc="upper right")
axes[1].legend(loc="upper right")
axes[2].legend(loc="upper right")
axes[0].set(yticklabels=[])  
axes[0].tick_params(left=False, bottom=False)
axes[1].set(yticklabels=[])  
axes[1].tick_params(left=False, bottom=False) 
axes[2].set(yticklabels=[])  
axes[2].tick_params(left=False, bottom=True)
axes[2].text(0.2, 0.025, 'x2.2', font=font, fontsize=14)
axes[0].text(0.9, 0.9, '(b)', font=font, fontsize=14)      
fig.supxlabel("Chemical Shift [ppm]", fontsize=12)
plt.savefig("1ds_stacked-left.png", dpi=300)
plt.show()