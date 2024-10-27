import numpy as np
from matplotlib import pyplot as plt, colors
import pandas as pd

#Cs - w1=50KHz
amplitudes = np.array([7.98, 7.95, 7.91, 7.72, 6.24, 4.62,  3.45, 2.68, 2.25])
freq = np.array([50, 50, 50, 51.466, 58.720, 169.779 ,181.488, 190.114, 196.850])
CQ = np.array([1, 50, 100, 250, 1000, 2500,  5000, 10000, 25000])

# Na - w1=50KHz
#CQ = np.array([1000, 10000, 50000, 250000, 1000000, 2500000, 5000000, 10000000])
#amplitudes = np.array([2.02, 2.014, 1.960, 1.661, 1.195, 1.069, 1.03, 0.958])
#freq = np.array([50000, 50000, 50000, 73583, 95419, 99206, 99900, 100000])

WQ = CQ/14
w1 = 50000
fig, ax1 = plt.subplots()
ax1.set_xscale("log")

color = 'tab:red'
plt.title("SQ Nutation (\u03C91=50kHz)")
ax1.set_xlabel("\u03C9q [kHz]")
ax1.set_ylabel("Nutation Frequency [kHz]", color=color)
ax1.scatter(WQ, freq, color=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel("Maximal Amplitude of Signal", color=color)
ax2.plot(WQ, amplitudes, 'o:', color=color)

#plt.legend(["\u03C91=50KHz"], loc="upper left")

plt.savefig("final-graph-Cs", dpi=300)
plt.show()