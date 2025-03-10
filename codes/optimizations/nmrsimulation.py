import fileinput
import sys
import os
import math 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.system("rm *.fid")  
filename = "test.fid"
baseline = open("baseline.txt", "r").read().split(",")
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


def replacement(lineNum, content):
  data = open('test.in', 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open('test.in', 'w')
  fileq.writelines(data)

def runSimulations(index1, index2, indexTau, prevT1, prevT2):
  replacement(ksjdgfklsdhbgladhfug;livuesohnth ) #all variables
  os.system("simpson zfilter_base.in")
  return (math.sqrt((np.loadtxt(filename,usecols=(1))[0])**2+((np.loadtxt(filename,usecols=(2))[0])**2)))/Integral0 
