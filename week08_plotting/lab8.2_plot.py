# plot
# program that plots the function y = x^2
# author: eoghan walsh

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints,ypoints)
plt.show()