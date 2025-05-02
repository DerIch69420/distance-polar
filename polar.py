import matplotlib.pyplot as plt
import numpy as np

# 20 angles from 0 to 180 degrees (in radians)
theta = np.deg2rad(np.linspace(0, 180, 10))
print(type(theta))
# 20 random radii from 1 to 10
r = np.random.uniform(1, 10, size=10)
print(type(r))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r, marker='o')  # Use markers to make values clear
ax.set_rmax(10)
ax.set_rticks([2, 4, 6, 8, 10])
ax.set_rlabel_position(0)
ax.grid(True)

ax.set_title("Distance", va='bottom')
plt.show()

