#!/usr/bin/env python3
"""
Plots a scatter plot of men's height versus weight.
Parameters:
    None
Returns:
    None
"""
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180
plt.title("Men's Height vs Weight")
plt.xlabel("Height (in)")
plt.ylabel("Weight (lbs)")
plt.yticks(np.arange(170, 191, 10))
plt.ylim(165, 195)
plt.xticks(np.arange(60, 81, 10))
plt.xlim(55, 85)
plt.scatter(x, y, color="magenta", s=9)
plt.show()
