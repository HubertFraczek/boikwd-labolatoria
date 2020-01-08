import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[5.6, 3.2, 4.4, 4.7, 100],
		[6, 3.5, 4.6, 4.5, 100],
		[100, 4, 5, 4.8, 100],
		[100, 3.8, 4.7, 4.8, 100],
		[4.8, 4, 4.5, 4.2, 100]])

row_ind, col_ind = linear_sum_assignment(cost)

for i in range(len(col_ind)):
    print("bank numer: ", i, "lokata numer: ", col_ind[i])

