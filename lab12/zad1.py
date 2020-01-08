import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[5,7,8,7], [6,4,7,6], [7,5,6,5], [4,3,5,9]])


row_ind, col_ind = linear_sum_assignment(cost)

#print(row_ind, col_ind)

for i in range(len(col_ind)):
    print("pracownik ", i, "powinien wykonać prace numer: ", col_ind[i])

