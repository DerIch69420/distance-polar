import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.title("Basic Plot")
plt.xlabel("x")
plt.ylabel("y = x^2")
plt.grid(True)
plt.show()

