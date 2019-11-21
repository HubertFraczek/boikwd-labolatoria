import numpy as np
from scipy.optimize import linprog
import math

A = [[1, 1, 1], [-1, -1, -1], [-1, -2, -1], [0, 2, 1], [-1, 0, 0], [0, -1, 0],
    [0, 0, -1]]
b = [30, -30, -10, 20, 0, 0, 0]
c = [-2, -1, -3]

res = linprog(c, A, b).x
f = 2 * res[0] + res[1] + 3 * res[2]

print(round(res[0]), round(res[1]), round(res[2]))
print(round(f))
