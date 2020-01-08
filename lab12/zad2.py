import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[0.8, 0.8, 0.8, 0.6, 0.6, 0.6],
		[2, 2, 2, 1.5, 1.5, 1.5],
		[0.7, 0.7, 0.7, 0.6, 0.6, 0.6],
		[0.4, 0.4, 0.4, 0.2, 0.2, 0.2],
		[0.2, 0.2, 0.2, 0.4, 0.4, 0.4],
		[0.3, 0.3, 0.3, 0.5, 0.5, 0.5]])

row_ind, col_ind = linear_sum_assignment(cost)

#print(row_ind, col_ind)

for i in range(0, 3):
    print("pracownik ", 0, "powinien wykonać prace numer: ", col_ind[i])

for i in range(3, len(col_ind)):
    print("pracownik ", 1, "powinien wykonać prace numer: ", col_ind[i])

