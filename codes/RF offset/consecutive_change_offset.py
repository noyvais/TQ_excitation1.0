import fileinput
import sys
import os
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes 
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from matplotlib.ticker import MaxNLocator
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle

left = 0
right = 0
step = 0
CQ = np.array([25, 250, 1000])

def generateParams():
  global left
  global right
  global step
  left = float(input("Enter minimal value for your parameter"))
  right = float(input("Enter maximal value for your parameter"))
  step = float(input("Enter step size for your parameter"))
  return np.arange(left, right+step, step).tolist()

file = "offset_base.in"
"""
offsetParams = generateParams()
prevShift = shiftParams[0]
nextShift = shiftParams[0]
"""
offsetParams = generateParams()
prevOffset = offsetParams[0]
nextOffset = offsetParams[0]
shiftline = 5
shiftline2 = 22
offset_line = 32
index = 0
shift_baseline = "shift 1 "
offset_baseline = "offset "
shift_baseline2 = "p 0 0 0 0 0"
CQline = 4
cq_baseline = "quadrupole 1 1 "
cq_baseline2 = " 0.6 0 0 0"
norm = 42
x1 = -15
x2 = 40
y1 = -0.01
y2 = 0.002

def replacement(lineNum, content):
  data = open('offset_base.in', 'r').readlines()
  data[lineNum-1] = '{}\n'.format(content)
  fileq =  open('offset_base.in', 'w')
  fileq.writelines(data)
 
def runSimulations(index, prevOffset):
  for i in range(len(CQ)):   
    replacement(CQline, cq_baseline + str(CQ[i]*1000) + cq_baseline2)
    index=0
    while (index <= len(offsetParams)):
      os.system("simpson offset_base.in")
      index = index+1
      nextOffset = offsetParams[index if index < len(offsetParams) else 0]
      """
      print("prev shift=", prevShift, "next shift=", nextShift) 
      replacement(shiftline, shift_baseline + str(prevShift) + shift_baseline2)
      replacement(shiftline2, "variable shift " + str(prevShift))
      prevShift = nextShift 
      """
      print("prev offset=", prevOffset, "next offset=", nextOffset)
      replacement(offset_line, offset_baseline + str(prevOffset))
      replacement(shiftline2, "variable shift " + str(prevOffset))
      prevOffset = nextOffset
      filenames = [f for f in os.listdir("./") if f.endswith('.fid')]
    filenames = sorted(filenames, key=os.path.getmtime)
    first_points = [(np.loadtxt(filename,usecols=(1))) for filename in filenames]
    first_points_arr = np.array(first_points)/norm
    ax.plot(np.array(offsetParams)/1000, first_points_arr, label="Cq="+str(CQ[i])+"kHz")
    #axins.plot(shiftParams, first_points_arr)
  print("simulations done!")

ax = plt.axes()  
#axins = zoomed_inset_axes(ax, 2, loc='lower center')
#mark_inset(ax, axins, loc1=2, loc2=3, fc="none", ec="0.5")
#axins.set_xlim(x1, x2)
#axins.set_ylim(y1, y2)
#axins.tick_params(labelleft=False, labelbottom=False)
replacement(offset_line, offset_baseline + str(prevOffset))
replacement(shiftline2, "variable shift " + str(prevOffset))
runSimulations(index, prevOffset)
#ax.add_patch(Rectangle((x1,y1),60,0.0125,
#                    alpha=0.1,
#                    facecolor='black',
#                    zorder=2))
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.legend()
plt.xlabel("Off Resonance [kHz]")
plt.savefig("rf-offset")
plt.show()
