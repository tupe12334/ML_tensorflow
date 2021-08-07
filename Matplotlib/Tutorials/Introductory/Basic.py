import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])

plt.plot([8,0], [0,4])
plt.plot([3,8], [0,0])
plt.plot([3,0], [0,4])
plt.plot([3,7], [0,8])
plt.plot([8,7], [0,8])
lineone =[[0,4],[7,8]]
plt.plot(*zip(*lineone))
# plt.plot([0,7], [4,8],marker = 'o')
# plt.axline((0,4), (7,8))
plt.title("test")
plt.show()

# x = np.linspace(0, 2, 100)

# # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
# fig, ax = plt.subplots()  # Create a figure and an axes.
# ax.plot(x, x, label='linear')  # Plot some data on the axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x label')  # Add an x-label to the axes.
# ax.set_ylabel('y label')  # Add a y-label to the axes.
# ax.set_title("Simple Plot")  # Add a title to the axes.
# ax.legend()  # Add a legend.