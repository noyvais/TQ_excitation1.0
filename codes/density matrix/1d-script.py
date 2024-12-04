import fileinput
import sys
import os
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import time

left = 0
right = 0
step = 0

def generateParams():
  global left
  global right
  global step
  left = float(input("Enter minimal value for your parameter"))
  right = float(input("Enter maximal value for your parameter"))
  step = float(input("Enter step size for your parameter"))
  return np.arange(left, right+step, step).tolist()

file = "base.in"
T1params_to_change = generateParams()
prevT1 = T1params_to_change[0]
nextT1 = T1params_to_change[0]
T1line = 19
index = 0
T1_baseline = "variable T2 "

def replacement(lineNum, content):
  data = open('2pls.in', 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open('2pls.in', 'w')
  fileq.writelines(data)
 
def runSimulations(index, prevT1):     
  while (index < len(T1params_to_change)):
    os.system("simpson 2pls.in")
    time.sleep(0.5)
    index = index+1
    nextT1 = T1params_to_change[index if index < len(T1params_to_change) else 0]
    print("prev T1=", prevT1, "next T1=", nextT1) 
    replacement(T1line, T1_baseline + str(prevT1))
    prevT1 = nextT1
    time.sleep(0.5)
  print("simulations done!")
      
replacement(T1line, T1_baseline + str(prevT1))
runSimulations(index, prevT1)