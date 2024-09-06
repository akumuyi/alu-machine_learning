#!/usr/bin/env python3
"""
Plots a bar chart showing the number of fruit per person.
Parameters:
    None
Returns:
    None
Raises:
    None
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# your code here
persons = (
    "Farrah",
    "Fred",
    "Felicia"
)

fruits = (
    "Apples",
    "Bananas",
    "Oranges",
    "Peaches"
)

color = [
    "red",
    "yellow",
    "#ff8000",
    "#ffe5b4"
]
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(3)

for i in range(4):
    p = ax.bar(persons, fruit[i], width, label=fruits[i], bottom=bottom, color=color[i])
    bottom += fruit[i]

ax.set_title("Number of Fruit per Person")
ax.set_ylabel("Quantity of Fruit")
ax.set_yticks(np.arange(0, 81, 10))
ax.set_ylim(0, 80)
ax.legend(loc="upper right")

plt.show()
