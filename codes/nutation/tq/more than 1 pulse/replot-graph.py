import numpy as np 
import matplotlib.pyplot as plt

firstT1 = 0.2
lastT1= 20
STEPx = 0.2
STEPy = 0.2
firstT2= 0.2
lastT2= 20
CQ = np.array([10000, 250000])
normalization=41.8619

for cq in CQ:
  intensities = (np.loadtxt("CQ="+str(cq)+".csv", delimiter=" ", dtype=float))/normalization
  plt.matshow(intensities) 
  x = np.arange(firstT2, lastT2+STEPx, STEPx) #the grid to which the x data corresponds
  x = np.around(x, decimals=2)
  nx = x.shape[0]
  step_x = 10 # step between consecutive labels
  x_positions = np.arange(4,nx,step_x) # pixel count at label position
  x_labels = x[4::step_x].astype(int) # labels you want to see
  y = np.arange(firstT1, lastT1+STEPy, STEPy) #the grid to which the y data corresponds
  y = np.around(y, decimals=2)
  ny = y.shape[0]
  step_y = 10
  y_positions = np.arange(4,ny,step_y) 
  y_labels = y[4::step_y].astype(int)
  plt.xticks(x_positions, x_labels)
  plt.yticks(y_positions, y_labels)
  cbar = plt.colorbar(fraction=0.045)
  cbar.formatter.set_powerlimits((-2, 2))
  cbar.formatter.set_useMathText(True)
  plt.ylabel("t1 [\u03bcs]")
  plt.xlabel("t2/3/4 [\u03bcs]")
  plt.savefig("CQ="+str(cq)+"-final.png", bbox_inches='tight', dpi=300)