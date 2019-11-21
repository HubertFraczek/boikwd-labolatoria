import numpy as np
from scipy.optimize import linprog

A = [[-5, -15], [-20, -5], [15, 2], [-1, 0], [0, -1]]
b = [-50, -40, 60, 0, 0]
c = [8, 4]

res = linprog(c, A, b).x
f = 8 * res[0] + 4 * res[1]

print(res[0], res[1])
print(f)
