import fileinput
import sys
import os
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

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

file = "nutation.in"
T1params = open("params.txt", "r")
T1params_to_change = generateParams()
prevT1 = T1params_to_change[0]
nextT1 = T1params_to_change[0]
T1line = 18
index = 0
T1_baseline = "variable T1 "

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
      
replacement(T1line, T1_baseline + str(prevT1))
runSimulations(index, prevT1)

filenames = [f for f in os.listdir("./") if f.endswith('.fid')]
filenames = sorted(filenames, key=os.path.getmtime)
filenames.reverse()
first_points = [(np.loadtxt(filename,usecols=(1))) for filename in filenames]
first_points_arr = np.array(first_points)

plt.plot(first_points_arr);
plt.title("intensity of signal VS Pulse duration")
plt.savefig("nutation")
plt.show()

yf = np.fft.fft(first_points_arr)
n = len(first_points_arr)
sampling_frequency = step*1e-6
frequencies = np.fft.fftfreq(n, sampling_frequency)

plt.plot(frequencies, yf);
plt.title("intensity of signal VS Pulse duration")
plt.xlabel("frequency [Hz]")
plt.ylabel("Intensity of Signal")
plt.savefig("fft")
plt.show()