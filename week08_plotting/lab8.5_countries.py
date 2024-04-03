# countries
# program that makes a pie chart of a list of countries
# author: eoghan walsh

import numpy as np
import matplotlib.pyplot as plt

counties = ["Cork", "Kerry", "Clare", "Tipperary", "Limerick", "Waterford"]
#num_of_counties = [500, 50, 300, 60, 70, 180]

num_of_counties = np.random.choice(counties, size = 100)

unique, counts = np.unique(num_of_counties, return_counts=True)

#num_of_counties = np.random.randint(1,7,100)

unique, counts = np.unique(num_of_counties, return_counts=True)

#plt.pie(counts, labels = unique)

plt.bar(unique,counts)

plt.show()