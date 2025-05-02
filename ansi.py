import matplotlib.pyplot as plt
import numpy as np

r = np.arange(0, 2, 0.01)
fdfd
#r = np.arange(0, 2, 0.01)
#r = list(range(0, 20, 0.1))/10
r = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
theta = 2 * np.pi * r

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
