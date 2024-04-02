# salaries & ages scatter plot
# program that makes a list of 10 random numbers
#   between 20,000 and 80,000 and 10 random ages between 21 and 65
#   and plots in a scatter plot.
# author: eoghan walsh

import numpy as np
import matplotlib.pyplot as plt

salary_low = 20000
salary_high = 80000
salary_size = 10

age_low = 21
age_high = 65
age_size = 10

np.random.seed(1)
salaries = np.random.randint(salary_low, salary_high, salary_size)
ages = np.random.randint(age_low, age_high, age_size)

plt.scatter(ages, salaries)
plt.show()