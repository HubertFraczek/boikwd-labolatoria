import numpy as np
from scipy.optimize import linprog

A = [[-1, -4],
    [-3, -6],
    [-2, -5],
    [-3, -7],
    [-1, -1]]

c = [6, 15]

b = [-2, -5, -3, -4, -1]

res = linprog(np.transpose(c), A, b).x

print(res)
