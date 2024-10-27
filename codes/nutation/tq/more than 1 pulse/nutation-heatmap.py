import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

left = 0
right = 0
CQ = np.array([10000])
STEPx = 0
STEPy = 0

def generateParams(axis = None):
  global left
  global right
  global step
  left = float(input("Enter minimal value for your parameter"))
  right = float(input("Enter maximal value for your parameter"))
  step = float(input("Enter step size for your parameter"))
  global STEPx, STEPy
  if axis == "x": STEPx = float(step)
  elif axis =="y": STEPy = float(step)
  return np.arange(int(left), int(right)+float(step), float(step)).tolist()

os.system("rm *.fid")  
T1params_to_change = generateParams("y")
T2params_to_change = generateParams("x")
file = "nutation.in"
prevT1 = T1params_to_change[0]
nextT1 = T1params_to_change[0]
prevT2 = T2params_to_change[0]
nextT2 = T1params_to_change[0]
prevCQ = CQ[0]
nextCQ = CQ[0]
index1 = 0
index2 = 0
CQ_index = 0
T1line = 18  
T2line = 19
CQline = 4
T1_baseline = "variable T1 "
T2_baseline = "variable T2 "
CQ_baseline = "quadrupole 1 1 "
CQ_baseline2 = " 0.6 0 0 0"

def replacement(lineNum, content):
  data = open('nutation.in', 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open('nutation.in', 'w')
  fileq.writelines(data)
 
def runSimulations(index1, index2, CQ_index, prevT1, prevT2):     
  for i in range(len(CQ)):
    while (index1 < len(T1params_to_change)):
      while (index2 < len(T2params_to_change)):
          os.system("simpson nutation.in")
          index2 = index2 + 1
          nextT2 = T2params_to_change[index2 if index2 < len(T2params_to_change) else index2-1]
          print("prev:", prevT2, "next:", nextT2)
          replacement(T2line, T2_baseline + str(nextT2))
          prevT2 = nextT2
      print("done with T2 parameters for T1:", prevT1)
      index2 = 0
      index1 = index1+1
      nextT1 = T1params_to_change[index1 if index1 < len(T1params_to_change) else 0]
      nextT2 = T2params_to_change[index2]
      print("prev T1=", prevT1, "next T1=", nextT1) 
      replacement(T1line, T1_baseline + str(nextT1))
      replacement(T2line, T2_baseline + str(nextT2))
      prevT1 = nextT1
      prevT2 = nextT2
    print("simulations done!")
    intensities = np.zeros(shape=(len(T1params_to_change),len(T2params_to_change)))
    filenames = [f for f in os.listdir("./") if f.endswith('.fid')]
    filenames = sorted(filenames, key=os.path.getmtime)
    first_points = [np.loadtxt(filename,usecols=(1)) for filename in filenames]
    first_points_arr = np.array(first_points)
    intensities = np.reshape(first_points_arr, (len(T1params_to_change), len(T2params_to_change)))
    df = pd.DataFrame(data=intensities.astype(float))
    df.to_csv("CQ="+str(CQ[CQ_index])+".csv", sep=' ', header=False, float_format='%.3f', index=False)
    plt.matshow(intensities)
    x = np.arange(T2params_to_change[0], (T2params_to_change[-1]+STEPx), STEPx) #the grid to which the x data corresponds
    nx = x.shape[0]
    step_x = 4 # step between consecutive labels
    x_positions = np.arange(0,nx,step_x) # pixel count at label position
    x_labels = x[::step_x] # labels you want to see
    y = np.arange(T1params_to_change[0], (T1params_to_change[-1]+STEPy), STEPy) #the grid to which the y data corresponds
    ny = y.shape[0]
    step_y = 4 
    y_positions = np.arange(0,ny,step_y) 
    y_labels = y[::step_y]
    plt.xticks(x_positions, x_labels)
    plt.yticks(y_positions, y_labels)
    plt.colorbar()
    plt.title("Pulse durations VS intensity of signal")
    plt.xlabel("duration of each of the last 3 pulses")
    plt.ylabel("duration of first pulse")
    plt.savefig("CQ="+str(CQ[CQ_index])+".png")
  # plt.show()
    os.system("rm *.fid") 
    CQ_index = CQ_index + 1
    nextCQ = CQ[CQ_index if CQ_index < len(CQ) else 0]
    replacement(CQline, CQ_baseline + str(nextCQ) + CQ_baseline2)
    prevT1 = T1params_to_change[0]
    prevT2 = T2params_to_change[0]
    index1 = 0
    index2 = 0

replacement(T1line, T1_baseline + str(prevT1))
replacement(T2line, T2_baseline + str(prevT2))
#replacement(T2line, T2_baseline + str(prevT2))
runSimulations(index1, index2, CQ_index, prevT1, prevT2)