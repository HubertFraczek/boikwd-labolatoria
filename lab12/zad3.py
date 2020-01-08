import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[5.6, 3.2, 4.4, 4.7, 0],
		[6, 3.5, 4.6, 4.5, 0],
		[0, 4, 5, 4.8, 0],
		[0, 3.8, 4.7, 4.8, 0],
		[4.8, 4, 4.5, 4.2, 0]])

row_ind, col_ind = linear_sum_assignment(cost*(-1))

for i in range(len(col_ind)):
    print("bank numer: ", i, "lokata numer: ", col_ind[i])
print(cost[row_ind, col_ind].sum())

