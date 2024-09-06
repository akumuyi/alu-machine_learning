#!/usr/bin/env python3
"""
Plot a line graph of the cube of numbers from 0 to 10.
This script uses the NumPy and Matplotlib libraries to generate a line graph of the cube of numbers from 0 to 10.
"""
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
plt.plot(y, color='red')
plt.xticks(np.arange(0, 11, 2))
plt.xlim(0, 10)
plt.yticks(np.arange(0, 1001, 200))
plt.ylim(-50, 1050)
plt.show()