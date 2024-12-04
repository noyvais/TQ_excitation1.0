import numpy as np
from matplotlib import pyplot as plt, colors
import pandas as pd

#Cs - w1=5KHz
amplitudes = np.array([8.00, 7.99, 7.98, 7.87, 6.64, 4.81, 3.62, 2.78, 2.28, 2.03])
freq = np.array([5000, 5000, 5000, 5050, 6097, 8928, 12626, 16447, 19231, 20000])
CQ = np.array([100, 5000, 10000, 25000, 100000, 250000,  500000, 1000000, 2500000, 10000000])

# Na - w1=5KHz
#CQ = np.array([100, 1000, 5000, 25000, 100000, 250000, 500000, 1000000])
#amplitudes = np.array([2.02, 2.014, 1.983, 1.749, 1.21, 1.089, 1.041, 1.018])
#freq = np.array([5000, 5000, 5050, 5882, 8680, 9328, 9690, 9960])

#Cs - w1=50KHz
#amplitudes = np.array([7.98, 7.95, 7.91, 7.72, 6.24, 4.62,  3.45, 2.68, 2.25])
#freq = np.array([50000, 50000, 50000, 51466, 58720, 169779 ,181488, 190114, 196850])
#CQ = np.array([1000, 50000, 100000, 250000, 1000000, 2500000,  5000000, 10000000, 25000000])

# Na - w1=50KHz
#CQ = np.array([1000, 10000, 50000, 250000, 1000000, 2500000, 5000000, 10000000])
#amplitudes = np.array([2.02, 2.014, 1.960, 1.661, 1.195, 1.069, 1.03, 0.958])
#freq = np.array([50000, 50000, 50000, 73583, 95419, 99206, 99900, 100000])

#Cs - w1=500KHz
#amplitudes = np.array([8.03, 7.96, 7.91 ,7.70, 6.24, 4.62, 3.52, 2.73, 2.24])
#freq = np.array([500000, 500000, 506072, 521648, 666667, 925926, 1240694, 1945525, 2000000])
#CQ = np.array([10000, 500000, 1000000, 2500000, 10000000, 25000000,  50000000, 100000000, 250000000])

# Na - w1=500KHz
#CQ = np.array([10000, 100000, 500000, 2500000, 10000000, 25000000, 50000000, 100000000])
#amplitudes = np.array([2.01, 2.005, 1.960, 1.661, 1.192, 1.055, 0.994, 0.973])
#freq = np.array([500000, 500000, 512820, 776397, 968992, 983284, 997008, 1000000])


WQ = CQ/14
w1 = 500000

df = pd.DataFrame({"x": WQ, "y": freq, "color": amplitudes})
fig, ax = plt.subplots()
cmap = plt.cm.viridis
norm = colors.Normalize(vmin=2.28, vmax=8)
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
plt.savefig("graph-Cs")
plt.show()