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

CQline = 5
Qline = 19
CQ_index = -1
CQ_baseline = "quadrupole 1 1 "
CQ_baseline2 = " 0 0 0 0"
Q_baseline = "variable q "
leftppm=649.51
rightppm=-622.21
size=8192
leftkHz=51
rightkHz=-48.8
labels = ['(a)','(b)','(c)','(d)']

CQ= numpy.array([500, 250, 150])
data_static = numpy.loadtxt('Zeolites-static.txt',skiprows=3016, max_rows=2192)
data_mas = numpy.loadtxt('Zeolites-mas.txt',skiprows=3010, max_rows=2192)
#data_static = numpy.loadtxt('Zeolites-static.txt',skiprows=10)
#data_mas = numpy.loadtxt('Zeolites-mas.txt',skiprows=10)
data_mas = 1.2*data_mas

def replacement(lineNum, content):
  data = open('static_base.in', 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open('static_base.in', 'w')
  fileq.writelines(data)
  datam = open('mas_base.in', 'r').readlines()
  datam[lineNum-1] = '{}\n'.format(content)
  fileqm =  open('mas_base.in', 'w')
  fileqm.writelines(datam)

fig, axes = plt.subplots(1,CQ.shape[0]+1, figsize=(13, 6), gridspec_kw = {'wspace':0.05})

for i in range(len(CQ)):
  CQ_index = CQ_index+1
  axes[i].annotate(labels[i], xy=(0.03, 0.95), xycoords="axes fraction", font=font, fontsize=14)
  #replacement(CQline, CQ_baseline + str(CQ[CQ_index if CQ_index < len(CQ) else 0]*1000) + CQ_baseline2)
  #replacement(Qline, Q_baseline + str(CQ[CQ_index if CQ_index < len(CQ) else 0]))
  #os.system("simpson static_base.in")
  #os.system("simpson mas_base.in")
  x = numpy.loadtxt('static_base'+str(CQ[i])+'.spe', usecols=(0), skiprows=512, max_rows=1024)/1000
  y = numpy.loadtxt('static_base'+str(CQ[i])+'.spe', usecols=(1), skiprows=512, max_rows=1024)
  xm = numpy.loadtxt('mas_base'+str(CQ[i])+'.spe', usecols=(0), skiprows=512, max_rows=1024)/1000
  ym = numpy.loadtxt('mas_base'+str(CQ[i])+'.spe', usecols=(1), skiprows=512, max_rows=1024)
  axes[i].plot(xm, ym, label="MAS")
  axes[i].plot(x, y, label="Static")
  axes[i].set_title("Cq="+str(CQ[i])+"kHz", fontsize=12)
  axes[i].get_yaxis().set_visible(False)
  axes[i].set_ylim(-100,1600)
  axes[i].set_xlim(-9.5, 9.5)
  axes[i].legend(loc="upper right")
  axes[i].xaxis.set_major_locator(plt.MaxNLocator(5))
  axes[i].invert_xaxis()
  """
  x = numpy.linspace(-15, 15, 1024) #the grid to which the x data corresponds
  nx = x.shape[0]
  step_x = 220 # step between consecutive labels
  x_positions = numpy.arange(10,nx,step_x) # pixel count at label position
  print(x_positions)
  x_labels = [10, 5, 0, -5, -10]
  axes[i].set_xticks(x_positions, x_labels)
  """
  plt.savefig("lineshapes"+str(CQ[i])+".png", dpi=300)


x = numpy.linspace(leftkHz, rightkHz, size) #the grid to which the x data corresponds
x = x[3000:-3000]
nx = x.shape[0]
step_x = 400 # step between consecutive labels
x_positions = numpy.arange(100,2000,step_x) # pixel count at label position
x_labels = [12, 8, 4, 0, -4]
axes[CQ_index+1].set_xlim(-6, 9)
axes[CQ_index+1].plot(data_mas, label='MAS')
axes[CQ_index+1].plot(data_static, label='Static')
axes[CQ_index+1].set_xticks(x_positions, x_labels)
axes[CQ_index+1].get_yaxis().set_visible(False)
axes[CQ_index+1].set_title("Experimental data", fontsize=12)
axes[CQ_index+1].legend(loc="upper right")
axes[CQ_index+1].annotate('*', xy=(535, 1.8e4), xytext=(535, 8e4), size=16, 
            arrowprops=dict(arrowstyle='->'), ha='center')
axes[CQ_index+1].annotate(labels[i+1], xy=(0.03, 0.95), xycoords="axes fraction", font=font, fontsize=14)            
fig.supxlabel("Chemical Shift [kHz]", fontsize=12)
plt.tight_layout()
#plt.savefig("mas-static.png", dpi=300)
plt.show()

