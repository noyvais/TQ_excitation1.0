import fileinput
import sys
import os
import math 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

STEPx = 0
STEPy = 0
STEPtau = 0

def generateParams(i, axis = None):
  left = float(sys.argv[i+1])
  right = float(sys.argv[i+2])
  step = float(sys.argv[i+3])
  global STEPx, STEPy
  if axis == "x": STEPx = step 
  elif axis =="y": STEPy = step
  else: STEPtau = step
  #print(np.arange(left, right+step, step).tolist())
  return np.arange(left, right+step, step).tolist()

os.system("rm *.fid")  
T1params_to_change = generateParams(0, "y")
T2params_to_change = generateParams(3, "x")
tau = generateParams(6)
file = "z-filter.in"
prevT1 = T1params_to_change[0]
prevT2 = T2params_to_change[0]
prevTAU = tau[0]
baseline = open("baseline.txt", "r").read().split(",")
print(baseline)
T1_baseline = baseline[0]
T2_baseline = baseline[1]
tau_baseline = baseline[2]
# the following lines are specific for T1, T2
index1 = 0
index2 = 0
indexTau = 0
T1line = 19
T2line = 20
TAUline = 18
# for normalization
Integral0 = 41.8626

print(T1_baseline + str(prevT1))

def replacement(lineNum, content):
  data = open('TQ_4pls-typo.in', 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open('TQ_4pls-typo.in', 'w')
  fileq.writelines(data)

def runSimulations(index1, index2, indexTau, prevT1, prevT2):     
  for i in range(len(tau)):
    while (index1 < len(T1params_to_change)):
      while (index2 < len(T2params_to_change)):
        os.system('simpson TQ_4pls-typo.in')
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
    first_points = [(math.sqrt((np.loadtxt(filename,usecols=(1))[0])**2+((np.loadtxt(filename,usecols=(2))[0])**2)))/Integral0 for filename in filenames]
    first_points_arr = np.array(first_points)
    intensities = np.reshape(first_points_arr, (len(T1params_to_change), len(T2params_to_change)))
    df = pd.DataFrame(data=intensities.astype(float))
    df.to_csv("TQE"+str(tau[indexTau])+".csv", sep=' ', header=False, float_format='%.5f', index=False)
    #plt.matshow(intensities)
    x = np.arange(T2params_to_change[0], (T2params_to_change[-1]+STEPx), STEPx) #the grid to which the x data corresponds
    nx = x.shape[0]
    step_x = 8 # step between consecutive labels
    x_positions = np.arange(0,nx,step_x) # pixel count at label position
    x_labels = x[::step_x] # labels you want to see
    y = np.arange(T1params_to_change[0], (T1params_to_change[-1]+STEPy), STEPy) #the grid to which the y data corresponds
    ny = y.shape[0]
    step_y = 4
    y_positions = np.arange(0,ny,step_y) 
    y_labels = y[::step_y]
    plt.xticks(x_positions, x_labels)
    plt.yticks(y_positions, y_labels)
    # normalize colorbar
    plt.pcolor(intensities, cmap="RdPu")
    plt.colorbar()
    plt.title("Intensity of signal VS Pulse durations")
    plt.xlabel("Second Pulse Duration")
    plt.ylabel("First Pulse Duration")
    plt.savefig("SC"+str(tau[indexTau])+".png")
    plt.clf()
    os.system("rm *.fid") 
    indexTau = indexTau + 1
    nextTau = tau[indexTau if indexTau < len(tau) else 0]
    replacement(TAUline, tau_baseline + str(nextTau))
    prevT1 = T1params_to_change[0]
    prevT2 = T2params_to_change[0]
    index1 = 0
    index2 = 0

replacement(T1line, T1_baseline + str(prevT1))
replacement(T2line, T2_baseline + str(prevT2))
replacement(T2line, T2_baseline + str(prevT2))
runSimulations(index1, index2, indexTau, prevT1, prevT2)