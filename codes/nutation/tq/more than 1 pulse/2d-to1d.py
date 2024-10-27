import numpy as np 
import matplotlib.pyplot as plt

firstT1 = 0
lastT1= 20
STEPx = 0.2
STEPy = 0.2
firstT2= 0
lastT2= 20
CQ = np.array([10000, 20000, 35000, 50000, 100000])
time_row = np.arange(firstT1, lastT1+STEPy, STEPy)
time_col = np.arange(firstT2, lastT2+STEPx, STEPx)

for cq in CQ:
  intensities = np.loadtxt("CQ="+str(cq)+".csv", delimiter=" ", dtype=float)
  maximal_coordinates = np.where(intensities == np.max(intensities)) # res is tuple of row and column where maximal value resides
  max_row = maximal_coordinates[0][0]
  max_col = maximal_coordinates[1][0]
  minimal_coordinates = np.where(intensities == np.min(intensities)) # res is tuple of row and column where minimal value resides
  min_row = minimal_coordinates[0][0]
  min_col = minimal_coordinates[1][0]
  max_col_plot = intensities[:, max_col]
  min_col_plot = intensities[:, min_col]
  max_row_plot = intensities[max_row]
  min_row_plot = intensities[min_row]
  
  fig, axs = plt.subplots(2, 2)
  axs[0, 0].plot(time_row, max_row_plot)
  axs[0, 0].set_title('Row of Maximal Intensity')
  axs[0, 1].plot(time_col, max_col_plot, 'tab:orange')
  axs[0, 1].set_title('Column of Maximal Intensity')
  axs[1, 0].plot(time_row, min_row_plot, 'tab:green')
  axs[1, 0].set_title('Row of Maximal Negative Intensity')
  axs[1, 1].plot(time_col, min_col_plot, 'tab:red')
  axs[1, 1].set_title('Column of Maximal Negative Intensity')

  for ax in axs.flat:
    ax.set(xlabel='Duration of Pulse', ylabel='Intensity')

  # Hide x labels and tick labels for top plots and y ticks for right plots.
  for ax in axs.flat:
    ax.label_outer()
    
  plt.savefig("1d-CQ="+str(cq)+".png")
  plt.show()
    
  