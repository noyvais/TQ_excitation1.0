import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

CQ = np.array([10, 60, 150, 300, 450])
schemes = np.array(['1pls', '2pls', '3pls', '4pls'])
signal = np.array([[0.00377, 0.00218, 0.00495, 0.00819], [0.019, 0.062, 0.13, 0.165], [0.09, 0.172, 0.18, 0.146], [0.13, 0.204, 0.134, 0.121], [0.101, 0.188, 0.102, 0.095]])

for i, cq in enumerate(CQ):
  plt.plot(schemes, signal[i, :], marker='o', label="Cq="+str(cq)+"KHz")
  for i, v in enumerate(signal[i, :]):
    if v == 0.134 or v==0.019:
      plt.annotate(str(v), xy=(i,v), xytext=(-7,7), textcoords='offset points', fontsize=8)
    elif v==0.101:
       plt.annotate(str(v), xy=(i,v), xytext=(-13,7), textcoords='offset points', fontsize=8)
    elif v==0.00218:
       plt.annotate(str(v), xy=(i,v), xytext=(0,7), textcoords='offset points', fontsize=8)
    elif v==0.00377 or v==0.00495:
       plt.annotate(str(v), xy=(i,v), xytext=(-1,7), textcoords='offset points', fontsize=8)
    elif v==0.00819:
       plt.annotate(str(v), xy=(i,v), xytext=(-20,-15), textcoords='offset points', fontsize=8)
    else:
      plt.annotate(str(v), xy=(i,v), xytext=(-10,-15), textcoords='offset points', fontsize=8)

plt.title("Maximal Signal per Cq Value Achieved by Each Pulse Scheme")
plt.legend(loc="center right", fontsize="8", bbox_to_anchor=(0.99,0.25))
plt.savefig("summaryplot_with10kHz.png", bbox_inches='tight', dpi=300)
plt.show()