#!/usr/bin/env python3
"""
Exponential Decay of Radioactive Elements
This script plots the exponential decay of two radioactive elements, C-14 and Ra-226, over time.
Parameters:
    None
Returns:
    None
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

plt.title("Exponential Decay of Radioactive Elements")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.yticks(np.arange(0, 2, 0.2))
plt.ylim(0, 1)
plt.xticks(np.arange(0, 21000, 2500))
plt.xlim(0, 20000)
plt.plot(x, y1, '--r', x, y2, '-g')
plt.legend(["C-14", "Ra-226"], loc= 1,)
plt.show()