import fileinput
import sys
import os
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from pyfonts import load_font

left = 0
right = 0
step = 0
#CQ = np.array([1000, 10000, 50000, 100000, 250000, 500000])
CQ = np.array([1000000, 2000000, 5000000, 10000000])
font = load_font(
   font_url="https://github.com/jondot/dotfiles2/blob/master/.fonts/cambria.ttf?raw=true"
)
def generateParams():
  global left
  global right
  global step
  left = float(input("Enter minimal value for your parameter"))
  right = float(input("Enter maximal value for your parameter"))
  step = float(input("Enter step size for your parameter"))
  return np.arange(left, right+step, step).tolist()

file = "nutation.in"
T1params_to_change = generateParams()
prevT1 = T1params_to_change[0]
nextT1 = T1params_to_change[0]
prevCQ = CQ[0]
nextCQ = CQ[0]
T1line = 18
CQline = 4
index = 0
CQ_index = 0
T1_baseline = "variable T1 "
CQ_baseline = "quadrupole 1 1 "
CQ_baseline2 = " 0.6 0 0 0"
norm = 8

def replacement(lineNum, content):
  data = open('nutation.in', 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open('nutation.in', 'w')
  fileq.writelines(data)
 
def runSimulations(index, prevT1):     
  while (index < len(T1params_to_change)):
    os.system("simpson nutation.in")
    index = index+1
    nextT1 = T1params_to_change[index if index < len(T1params_to_change) else 0]
    print("prev T1=", prevT1, "next T1=", nextT1) 
    replacement(T1line, T1_baseline + str(prevT1))
    prevT1 = nextT1
  print("simulations done!")

replacement(CQline, CQ_baseline + str(CQ[0]) + CQ_baseline2) 
data = np.array([])
while (CQ_index < len(CQ)):
  os.system("rm *.fid")      
  replacement(T1line, T1_baseline + str(prevT1))
  print("CQ={}".format(CQ[CQ_index]))
  print("CQ INDEX =   ", CQ_index)
  runSimulations(index, prevT1)
  
  filenames = [f for f in os.listdir("./") if f.endswith('.fid')]
  filenames = sorted(filenames, key=os.path.getmtime)
  first_points = [(np.loadtxt(filename,usecols=(1))) for filename in filenames]
  first_points_arr = np.array(first_points)/norm
  plt.plot(T1params_to_change[:-1], first_points_arr, label="Cq={}MHz".format(int(CQ[CQ_index]/1000000)))
  
  if CQ[CQ_index] < 50000:
    data = np.append(data, first_points_arr[:80])
  
  CQ_index = CQ_index+1
  replacement(CQline, CQ_baseline + str(CQ[CQ_index if CQ_index < len(CQ) else 0]) + CQ_baseline2)
  
plt.legend(loc="upper left")
plt.xlabel("Irradiation duration [\u03BCs]")
plt.ylim(-0.81, 0.76)
#locs, labels = plt.yticks()
#labels = np.linspace(-0.8, 0.7, len(locs))
labels_list = [0.6, 0.4, 0.2, 0, -0.2, -0.4, -0.6, -0.8]
#plt.setp(plt.gca(), yticks=[-0.6, -0.4, 0.-0.2, 0, 0.2, 0.4, 0.6])
plt.yticks(labels_list)
#plt.ylabel('TQ Signal')
plt.annotate('(b)', xy=(0.02, 0.03), xycoords="axes fraction", font=font, fontsize=14)
"""
ax2 = plt.axes([.73, .69, .16, .12])
ax2.plot(T1params_to_change[:80], data[0:80], T1params_to_change[:80], data[80:160])
ax2.ticklabel_format(style='sci',scilimits=(-2,2),axis='both')
plt.setp(ax2, xticks=[], yticks=[0.002, 0, -0.002], xlabel="", ylabel="")
ax2.set_title("Low Cq", loc="right")
"""
plt.savefig("high.png" ,dpi=300)
plt.show()