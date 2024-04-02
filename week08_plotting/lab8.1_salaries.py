# salaries
# program that makes a list of 10 random numbers
#   between 20,000 and 80,000.
# author: eoghan walsh

import numpy as np

range_low = 20000
range_high = 80000
size = 10

np.random.seed(1)
salaries = np.random.randint(range_low, range_high, size)
salaries_plus = salaries + 5000
salaries_mult = salaries * 1.05
salaries_new = salaries_mult.astype(int)
print(salaries)
print(salaries_plus)
print(salaries_mult)
print(salaries_new)