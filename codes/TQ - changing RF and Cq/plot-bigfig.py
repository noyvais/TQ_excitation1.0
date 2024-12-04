import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import matplotlib.gridspec as gridspec

firstT1 = 1
lastT1= 50
STEPx = 1
STEPy = 1
firstT2= 1
lastT2= 50
CQ = np.array([60, 150, 300, 450])
schemes = np.array(['2pls', '3p1', '3p2', '4p1', '4p2'])
taus = np.array([[50, 50, 100, 100], [25, 25, 100, 100], [50, 50, 100, 100], [50, 25, 50, 100], [50, 100, 100, 100]])

x = np.arange(firstT2, lastT2+STEPx, STEPx) #the grid to which the x data corresponds
nx = x.shape[0]
step_x = 20 # step between consecutive labels
x_positions = np.arange(19,nx,step_x) # pixel count at label position
x_labels = x[19::step_x] # labels you want to see
y = np.arange(firstT1, lastT1+STEPy, STEPy) #the grid to which the y data corresponds
ny = y.shape[0]
step_y = 20 
y_positions = np.arange(19,ny,step_y) 
y_labels = y[19::step_y]
cmap = cm.get_cmap('viridis')
normalizer = Normalize(0, 0.204) # normalize from minimal to maximal signal
im = cm.ScalarMappable(norm=normalizer)

custom_ylim=(1,50)
fig, axes = plt.subplots(schemes.shape[0], CQ.shape[0], sharex=True, sharey=True, gridspec_kw = {'wspace':-0.1, 'hspace':0.12})
plt.setp(axes, xticks=x_positions, xticklabels=x_labels, yticks=y_positions, yticklabels=y_labels, ylim=custom_ylim)

for indexscheme, scheme in enumerate(schemes):
  for indexcq, cq in enumerate(CQ):
    intensities = np.loadtxt(str(cq)+"KHz-"+scheme+".csv", delimiter=" ", dtype=float)
    axes[indexscheme, indexcq].imshow(intensities, cmap=cmap, norm=normalizer)
    axes[indexscheme, indexcq].text(0.2, 2.5, str(taus[indexscheme, indexcq]), color='white', fontsize=9)
    #if indexcq != 0 and indexscheme!=len(schemes)-1:
      #axes[indexscheme, indexcq].spines['left'].set_visible(False)
      #axes[indexscheme, indexcq].spines['bottom'].set_visible(False)
      #axes[indexscheme, indexcq].get_xaxis().set_visible(False)
      #axes[indexscheme, indexcq].set_xticks([])
    if indexscheme == 0:
      axes[indexscheme, indexcq].set_title("Cq="+str(cq)+"kHz", fontsize=8)
    #if indexscheme == len(schemes)-1:
   #   axes[indexscheme, indexcq].set_xlabel('Duration of each pulse in the second block [\u03bcs]', fontsize=10)
    if indexcq == len(CQ)-1:
      axes[indexscheme, indexcq].set_title("  "+str(scheme), loc="right", x=1, y=0.5, ha="left", va="center", fontsize=8)
fig.colorbar(im, ax=axes.ravel().tolist(), pad=0.1)
# only put axes on outermost subplots
for ax in axes.flat:
    ax.label_outer()

fig.text(0.5,0.04, "t\u2082 [\u03bcs]", ha="center", va="center")
fig.text(0.1,0.5, "t\u2081 [\u03bcs]", ha="center", va="center", rotation=90)
fig.suptitle("TQ Efficiency")  
plt.savefig("bigfig-withtau.png", bbox_inches='tight', dpi=300)
plt.show()
