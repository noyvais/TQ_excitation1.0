import fileinput
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


STEPx = 0
STEPy = 0
STEPtau = 0

def generateParams(axis = None):
  left = float(input("Enter minimal value for your parameter"))
  right = float(input("Enter maximal value for your parameter"))
  step = float(input("Enter step size for your parameter"))
  global STEPx, STEPy
  if axis == "x": STEPx = step 
  elif axis =="y": STEPy = step
  else: STEPtau = step
  #print(np.arange(left, right+step, step).tolist())
  return np.arange(left, right+step, step).tolist()

os.system("rm *.fid")  
T1params_to_change = generateParams("y")
T2params_to_change = generateParams("x")
tau = generateParams()
file = "base.in"
prevT1 = T1params_to_change[0]
prevT2 = T2params_to_change[0]
prevTAU = tau[0]
baseline = open("./baseline.txts", "r").read().split(",")
T1_baseline = baseline[0]
T2_baseline = baseline[1]
tau_baseline = baseline[2]
# the following lines are specific for T1, T2
index1 = 0
index2 = 0
indexTau = 0
T1line = 18  
T2line = 19
TAUline = 17
# for normalization
Integral0 = 41.8626

print(T1_baseline + str(prevT1))

def replacement(lineNum, content):
  data = open('2pls.in', 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open('2pls.in', 'w')
  fileq.writelines(data)

def runSimulations(index1, index2, indexTau, prevT1, prevT2):     
  for i in range(len(tau)):
    while (index1 < len(T1params_to_change)):
      while (index2 < len(T2params_to_change)):
          os.system("simpson 2pls.in")
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