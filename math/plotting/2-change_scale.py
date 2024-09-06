#!/usr/bin/env python3
"""
Exponential Decay of C-14
This script plots the exponential decay of C-14 over time. It uses the numpy and matplotlib libraries to generate the plot.
Parameters:
    None
Returns:
    None
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

plt.title("Exponential Decay of C-14")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.xticks(np.arange(0, 28651, 5000))
plt.xlim(0, 28650)
plt.semilogy(x, y)
plt.show()
