import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
from numpy.linalg import matrix_power 
matplotlib.rcParams['figure.figsize'] = 10, 10

Ip = np.zeros((8,8)) # specifically for spin 7/2
ones = np.ones((5)) # specifically for detecting 3Q
Ip= np.diag(ones, k=3) # specifically for detecting 3Q

i=0
folder_path = './'
for filename in os.listdir(folder_path):
  data_list = []
  if filename.endswith('.txt') and not filename.startswith('2p'):
    print(filename) 
    matrices=np.zeros((3200, 8, 8), dtype=np.complex128)
    data = open(filename, "r+")
    i=0
    for line in data:
      line = line.replace("{", " ")
      line = line.replace("}", " ")
      raw_data = line.split()
      data_list.extend(raw_data)
      data_list = [float(i) for i in data_list]
      real_data = data_list[::2]
      im_data = data_list[1::2]
      real_data_arr = np.array(real_data)
      im_data_arr = np.array(im_data)
      matrices[i] = np.reshape((real_data_arr+1j*im_data_arr), (8, 8))
      data_list = []
      i+=1
    density = np.mean(matrices, axis=0)
    trace = np.trace((np.dot(density, np.conjugate(Ip).T)))
    print("signal is: ", trace)
    fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [6, 1]})
    im = plt.imread('./pics/'+str(filename).strip('.txt')+'.png')
    mynorm = plt.Normalize(vmin=0, vmax=3.5)
    heatmap = ax[0].imshow(np.absolute(density), cmap='PuRd', norm=mynorm)
    for y in range(density.shape[0]):
      for x in range(density.shape[1]):
        ax[0].text(x, y, '%.3f' % np.absolute(density[y, x]), horizontalalignment='center', verticalalignment='center')
    ax[1].imshow(im)
    ax[1].axis('off')
    ax[1].set_anchor((0.25, 0.5))
    fig.colorbar(heatmap, ax=ax[0], norm=mynorm, shrink=0.8)
    plt.savefig(str(filename).strip('.txt')+'.png', dpi=300, bbox_inches="tight")
    plt.clf()