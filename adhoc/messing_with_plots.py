# messing with matplotlib
# author: eoghan walsh

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,21))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, '1')
plt.show()