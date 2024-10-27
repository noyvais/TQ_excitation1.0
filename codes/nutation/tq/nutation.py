import fileinput
import sys
import os
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

left = 0
right = 0
step = 0
CQ = np.array([250000])
""""""
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
normalization = 41.8626

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
  first_points_arr = np.array(first_points)/normalization
  plt.plot(T1params_to_change[:-1], first_points_arr, label="CQ={}KHz".format(int(CQ[CQ_index]/1000)))
  
  if CQ[CQ_index] < 50000:
    data = np.append(data, first_points_arr[:40])
  
  CQ_index = CQ_index+1
  replacement(CQline, CQ_baseline + str(CQ[CQ_index if CQ_index < len(CQ) else 0]) + CQ_baseline2)
  
plt.legend(loc="upper left")
plt.ylabel('TQ Signal')
plt.xlabel('Pulse duration [\u03bcs]')
plt.title("TQ Nutation")
#ax2 = plt.axes([.73, .69, .16, .12])
#ax2.plot(T1params_to_change[:40], data[0:40], T1params_to_change[:40], data[40:80])
#ax2.ticklabel_format(style='sci',scilimits=(-2,2),axis='both')
#plt.setp(ax2, xticks=[], yticks=[0, -0.00025], xlabel="", ylabel="")
#ax2.set_title("Low Cq", loc="right")
plt.savefig("just250.png" ,dpi=300)
plt.show()