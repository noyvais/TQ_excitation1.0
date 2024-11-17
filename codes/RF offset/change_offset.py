import fileinput
import sys
import os
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

left = 0
right = 0
step = 0
CQ = np.array([5, 10, 25])

def generateParams():
  global left
  global right
  global step
  left = float(input("Enter minimal value for your parameter"))
  right = float(input("Enter maximal value for your parameter"))
  step = float(input("Enter step size for your parameter"))
  return np.arange(left, right+step, step).tolist()

file = "offset_base.in"
shiftParams = generateParams()
prevShift = shiftParams[0]
nextShift = shiftParams[0]
shiftline = 5
shiftline2 = 22
index = 0
shift_baseline = "shift 1 "
shift_baseline2 = "p 0 0 0 0 0"
CQline = 4
cq_baseline = "quadrupole 1 1 "
cq_baseline2 = " 0.6 0 0 0"
norm = 42

def replacement(lineNum, content):
  data = open('offset_base.in', 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open('offset_base.in', 'w')
  fileq.writelines(data)
 
def runSimulations(index, prevShift):
  for i in range(len(CQ)):   
    replacement(CQline, cq_baseline + str(CQ[i]*1000) + cq_baseline2)
    index=0
    while (index <= len(shiftParams)):
      os.system("simpson offset_base.in")
      index = index+1
      nextShift = shiftParams[index if index < len(shiftParams) else 0]
      print("prev shift=", prevShift, "next shift=", nextShift) 
      replacement(shiftline, shift_baseline + str(prevShift) + shift_baseline2)
      replacement(shiftline2, "variable shift " + str(prevShift))
      prevShift = nextShift 
      filenames = [f for f in os.listdir("./") if f.endswith('.fid')]
    filenames = sorted(filenames, key=os.path.getmtime)
    first_points = [(np.loadtxt(filename,usecols=(1))) for filename in filenames]
    first_points_arr = np.array(first_points)/norm
    plt.plot(shiftParams, first_points_arr, label="Cq="+str(CQ[i])+"kHz")
  print("simulations done!")
      
replacement(shiftline, shift_baseline + str(prevShift) + shift_baseline2)
replacement(shiftline2, "variable shift " + str(prevShift))
runSimulations(index, prevShift)

plt.legend()
plt.xlabel("Off Resonance [ppm]")
plt.savefig("rf-offset")
plt.show()
