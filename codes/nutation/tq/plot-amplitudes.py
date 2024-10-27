import numpy as np
from matplotlib import pyplot as plt, colors
import pandas as pd

#TQ: Cs - w1=50KHz
amplitudes = np.array([0, 0.56, 2.01, 6.19,  4.28, 1.55, 1.15, 1.12, 0.94])
CQ = np.array([1000, 50000, 100000, 250000, 1000000, 2500000,  5000000, 10000000, 25000000])

# TQ: Na - w1=50KHz
#CQ = np.array([1000, 10000, 50000, 250000, 1000000, 2500000, 5000000, 10000000])
#amplitudes = np.array([0, 0.025, 0.578, 1.295, 0.601, 0.252, 0.131, 0.046])

WQ = CQ/14

plt.plot(CQ, amplitudes)
plt.xscale("log")
plt.title("Nutation Frequency as a Function of Wq")
plt.xlabel("Wq [Hz]")
plt.ylabel("Nutation Frequency")
plt.savefig("graph-Cs")
plt.show()