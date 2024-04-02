# salaries histogram
# program that makes a list of 10 random numbers
#   between 20,000 and 80,000 and plots in a histogram.
# author: eoghan walsh

import numpy as np
import matplotlib.pyplot as plt

range_low = 20000
range_high = 80000
size = 10

np.random.seed(1)
salaries = np.random.randint(range_low, range_high, size)

plt.hist(salaries)
plt.show()

