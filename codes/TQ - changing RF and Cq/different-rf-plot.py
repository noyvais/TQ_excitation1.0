import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from pyfonts import load_font

font = load_font(
   font_url="https://github.com/jondot/dotfiles2/blob/master/.fonts/cambria.ttf?raw=true"
)

labels=['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']
fig, axes = plt.subplots(2,3, gridspec_kw = {'wspace':0.05}, figsize=(9,6))
CQ = np.array([60, 150, 300, 450])
schemes = np.array(['1pls', '2pls', '3pls', '4pls'])
rf = np.array([10, 20, 70, 100, 150, 200])
signal = np.array([
[[0.019, 0.09167, 0.1164, 0.11211], [0.024, 0.11627, 0.1065, 0.10193], [0.009, 0.10538, 0.10734, 0.10488], [0.008, 0.06822, 0.08134, 0.08025]],
[[0.019, 0.06569, 0.12973, 0.1622], [0.063, 0.11904, 0.12975, 0.09857], [0.052, 0.11581, 0.10638, 0.09460], [0.048, 0.08187, 0.07696, 0.07034]],
[[0.019, 0.06567, 0.12691, 0.16062], [0.093, 0.17985, 0.19356, 0.16794], [0.162, 0.1931, 0.16451, 0.15536], [0.152, 0.24922, 0.14628, 0.13141]],
[[0.018,	0.06376,	0.12375,	0.15698], [0.009, 0.17509, 0.19825, 0.14551], [0.168, 0.17147, 0.17188, 0.16662], [0.164, 0.25238, 0.16093, 0.16445]],
[[0.018,	0.06567,	0.12858,	0.16325], [0.092,	0.17985,	0.20218,	0.16335], [0.17,	0.1931,	0.18006,	0.17269], [0.166,	0.14524,	0.17104,	0.16728]],
[[0.018,	0.06367, 0.12254, 0.14998], [0.088, 0.16457, 0.19750, 0.14259], [0.169, 0.16918, 0.1785, 0.16893], [0.169, 0.16912, 0.15250, 0.16933]]], dtype=object)
print(signal.shape)

for j, freq in enumerate(rf):
  for i, cq in enumerate(CQ):
    print(j)
    if j>2:
      axes[1, j-3].annotate(labels[j], xy=(0.03, 0.9), xycoords="axes fraction", font=font, fontsize=14)
      axes[1, j-3].plot(schemes, signal[j, i], marker='o')
      axes[1, j-3].set_ylim(0, 0.26)
    else:
      axes[0, j].plot(schemes, signal[j, i], marker='o', label="Cq="+str(cq)+"kHz")
      axes[0, j].annotate(labels[j], xy=(0.03, 0.9), xycoords="axes fraction", font=font, fontsize=14)
      axes[0, j].set_ylim(0, 0.26)
      if j==0:
        axes[0,j].legend(loc="upper right") 
    """
    if not j==0 and j<3:
      axes[0, j].get_yaxis().set_visible(False)
    elif j>=3:
      axes[1, j-3].get_yaxis().set_visible(False)    
    """  
  #  for i, v in enumerate(signal[i, :]):
  #    if v == 0.134 or v==0.019:
  #     plt.annotate(str(v), xy=(i,v), xytext=(-7,7), textcoords='offset points', fontsize=8)
  #    elif v==0.101:
  #       plt.annotate(str(v), xy=(i,v), xytext=(-13,7), textcoords='offset points', fontsize=8)
  #    else:
  #      plt.annotate(str(v), xy=(i,v), xytext=(-10,-15), textcoords='offset points', fontsize=8)
  
  #plt.title(f"Maximal Signal per Cq Value Achieved by Each Pulse Scheme (rf={rf[j]}kHz)")
  #plt.legend(loc="lower right")
  #plt.savefig(f"summaryplot_{j+5}.png", bbox_inches='tight', dpi=300)
for ax in axes.flat:
    ax.label_outer()
#plt.show()
plt.savefig('diff-rf.png', dpi=300)