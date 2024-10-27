import numpy as np
from matplotlib import pyplot as plt, colors
import pandas as pd

#Cs - w1=50KHz
#amplitudes = np.array([0.028, 0.58, 2.04, 5.35, 6.21, 4.43, 4.23])
#freq = np.array([50000, 50000, 50000, 50000, 50000, 52631, 59701])
#CQ = np.array([10000, 50000, 100000, 200000, 250000, 500000, 1000000])

# Na - w1=50KHz
CQ = np.array([10000, 50000, 100000, 250000])
amplitudes = np.array([0.024, 0.58, 1.272, 1.294])
freq = np.array([50000, 50000, 52631, 55928])

WQ = CQ/14
w1 = 500000

df = pd.DataFrame({"x": WQ, "y": freq, "color": amplitudes})
fig, ax = plt.subplots()
cmap = plt.cm.viridis
norm = colors.Normalize(vmin=0, vmax=1.294)
ax.scatter(df.x, df.y, color=cmap(norm(df.color.values)))
ax.set_xticks(df.x)
plt.xscale("log")
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
fig.colorbar(sm)
#plt.axhline(y=w1, c='black')
#plt.axhline(y=4*w1, c='black') 
plt.title("Nutation Frequency as a Function of Wq")
plt.xlabel("Wq [Hz]")
plt.ylabel("Nutation Frequency")
plt.savefig("nutation-graph-Na")
plt.show()