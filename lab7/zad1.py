import numpy as np
from scipy.optimize import linprog

c = [1, -1]
A = [[-1, 0], [2, 1]]
b = [20, 20]

x_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds])

x2 = res.x[0]
x3 = res.x[1]
x1 = 30 - x2 - x3
print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)
print("f =", 2*x1 +x2 + 3*x3)
print("f =", (-1)*(res.fun-60))

