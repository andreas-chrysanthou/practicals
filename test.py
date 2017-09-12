import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(−np.pi, np.pi, 100) # 100 points from −pi to pi inclusive
y1 = np.sin(x)
y2 = np.sin(3∗x)
plt.ion() # interactive mode on
plt.clf() # clear any existing figure
plt.plot(x, y1, label=’sin(x)’) # plot the first function with a legend
plt.plot(x, y2, label=’sin(3x)’) # and the second (over−plot)
plt.legend() # shows the legend
plt.grid() # show a grid
plt.xlabel(’x’) # insert this x label
plt.axis([x[0], x[−1],−1, 1]) # sets the axis ranges
