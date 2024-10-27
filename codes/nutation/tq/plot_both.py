import numpy as np
from matplotlib import pyplot as plt, colors
import pandas as pd

#Cs - w1=50KHz
amplitudes = np.array([0.028, 0.58, 2.04, 5.35, 6.21, 4.43, 4.23])
freq = np.array([50, 50, 50, 50, 50, 52.631, 59.701])
CQ = np.array([10, 50, 100, 200, 250, 500, 1000])

# Na - w1=50KHz
#CQ = np.array([10000, 50000, 100000, 250000])
#amplitudes = np.array([0.024, 0.58, 1.272, 1.294])
#freq = np.array([50000, 50000, 52631, 55928])

WQ = CQ/14
w1 = 50000
fig, ax1 = plt.subplots()
ax1.set_xscale("log")

color = 'tab:red'
plt.title("Single Pulse TQ Excitation Nutation")
ax1.set_xlabel("\u03C9q [KHz]")
ax1.set_ylabel("Nutation Frequency [KHz]", color=color)
ax1.scatter(WQ, freq, color=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel("Maximal Amplitude of Signal", color=color)
ax2.plot(WQ, amplitudes, color=color)

plt.legend(["\u03C91=50KHz"], loc="upper left")

plt.savefig("final-graph-Cs")
plt.show()