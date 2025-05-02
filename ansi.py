# https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html

import matplotlib.pyplot as plt
import numpy as np
import random

r_max = 100
r0 = 50
dr = 25
theta = np.arange(0, 1*np.pi+0.01, np.pi/100)
type(theta)               # https://numpy.org/doc/2.2/reference/generated/numpy.ndarray.html

r = np.zeros(len(theta))  # https://numpy.org/doc/2.2/reference/generated/numpy.matlib.zeros.html
r0 = 50
for i in range(len(theta)):
    r[i] = r0 + random.randint(-5,5)
    r0 = r[i]
    
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rmax(r_max)
ax.set_rticks(list(range(dr,r_max+1,dr)))  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Distance radar", va='top')
plt.show()
