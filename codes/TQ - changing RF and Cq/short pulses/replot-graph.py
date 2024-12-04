import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl

firstT1 = 0.2
lastT1= 20
STEPx = 0.2
STEPy = 0.2
firstT2= 0.2
lastT2= 20
CQ = np.array([10, 50, 250])
schemes = np.array(['2pls', '3pls', '4pls'])
normalization=41.8619
prevmin=0
prevmax=0
#cmaps=['PiYG','BrBG','PRGn']
cmaps=['viridis','viridis','viridis']

"""
for cq in CQ:
  for scheme in schemes:
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
    plt.ylabel("t\u2081 [\u03bcs]")
    plt.xlabel("t\u2082 [\u03bcs]")
    plt.savefig("CQ="+str(cq)+"-final.png", bbox_inches='tight', dpi=300)
    custom_ylim=(1,50)
"""
x = np.arange(firstT2, lastT2+STEPx, STEPx) #the grid to which the x data corresponds
x = np.around(x, decimals=2)
nx = x.shape[0]
step_x = 20 # step between consecutive labels
x_positions = np.arange(4,nx,step_x) # pixel count at label position
x_labels = x[4::step_x].astype(int) # labels you want to see
y = np.arange(firstT1, lastT1+STEPy, STEPy) #the grid to which the y data corresponds
y = np.around(y, decimals=2)
ny = y.shape[0]
step_y = 20
y_positions = np.arange(4,ny,step_y) 
y_labels = y[4::step_y].astype(int)

fig, axes = plt.subplots(schemes.shape[0], CQ.shape[0], sharex=True, sharey=True, gridspec_kw = {'wspace':0.12, 'hspace':0.2}, figsize=(8,6.5))
#fig = plt.figure()
#grid = AxesGrid(fig,211, nrows_ncols=(CQ.shape[0], schemes.shape[0]), share_all=True, cbar_mode="edge")
fig.tight_layout()
plt.setp(axes, xticks=x_positions, xticklabels=x_labels, yticks=y_positions, yticklabels=y_labels)

pc = [None] * 9
norm=[plt.Normalize(-0.085/normalization, 0.085/normalization), plt.Normalize(-1.2/normalization, 1.2/normalization), plt.Normalize(-3.731/normalization, 4.270/normalization)]

for indexcq, cq in enumerate(CQ):
  for indexscheme, scheme in enumerate(schemes):
    intensities = (np.loadtxt(str(scheme)+"CQ="+str(cq*1000)+".csv", delimiter=" ", dtype=float))/normalization
    axes[indexcq, indexscheme].pcolormesh(intensities, cmap=cmaps[indexcq], norm=norm[indexcq])
    if indexcq == 0:
      axes[indexcq, indexscheme].set_title(str(scheme), fontsize=8)
    if indexscheme == 0:
      axes[indexcq, indexscheme].text(1.5, 3,"Cq="+str(cq)+"kHz", fontsize=8, fontweight="bold")
        
cbar0 = fig.colorbar(mpl.cm.ScalarMappable(norm=norm[0], cmap=cmaps[0]), ax=axes[0,:])
cbar1 = fig.colorbar(mpl.cm.ScalarMappable(norm=norm[1], cmap=cmaps[1]), ax=axes[1,:])
cbar2 = fig.colorbar(mpl.cm.ScalarMappable(norm=norm[2], cmap=cmaps[2]), ax=axes[2,:])
cbar0.formatter.set_powerlimits((-2, 2))
cbar0.formatter.set_useMathText(True)
cbar1.formatter.set_powerlimits((-2, 2))
cbar1.formatter.set_useMathText(True)
cbar2.formatter.set_powerlimits((-1, 1))
cbar2.formatter.set_useMathText(True)
"""
intensities = np.empty((3,3,101,101))
norm=[plt.Normalize(), plt.Normalize(), plt.Normalize()]
for indexcq, cq in enumerate(CQ):
  for indexscheme, scheme in enumerate(schemes):
    intensities[indexcq, indexscheme] = (np.loadtxt(str(scheme)+"CQ="+str(cq*1000)+".csv", delimiter=" ", dtype=float))/normalization
  norm[indexcq] = plt.Normalize(vmin=min(np.min(intensities[indexcq, indexscheme-1], prevmin)), vmax=max(np.max(intensities[indexcq, indexscheme-1], prevmax)))
  print("hi")

k=-1  
for i in range(CQ.shape[0]):
  for j in range(schemes.shape[0]):
    k+=1
    normindex = 0 if k<CQ.shape[0] else (1 if k<2*CQ.shape[0] else 2)
    print("i",normindex)
    pc = grid[k].pcolormesh(intensities[i, j], cmap='viridis', norm=norm[normindex])
"""  
# only put axes on outermost subplots
#for ax in axes.flat:
#    ax.label_outer()

fig.text(0.5,0.04, "t\u2082 [\u03bcs]", ha="center", va="center")
fig.text(0.07,0.5, "t\u2081 [\u03bcs]", ha="center", va="center", rotation=90)
plt.savefig("nultiple-pulse-nutation.png", bbox_inches='tight', dpi=300)
plt.show()
