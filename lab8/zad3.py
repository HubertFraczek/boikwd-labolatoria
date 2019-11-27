import numpy as np
from scipy.optimize import linprog

conf = [(4, 0), (1, 1), (8, 0), (5, 1), (2, 2), (0, 3)]

A = np.array([[-4, 0],
    [-1, -1],
    [-8, 0],
    [-5, 1],
    [-2, -2],
    [0, -3]])

c = [12000, 18000]

b = np.array([-0.1, -0.2, -0.2, -0.3, -0.4, 0]) 

res = linprog(np.transpose(c), A, b).x

print(res)

A *= -1
b *= -1

def solve_(A, y, b):
    res = []
    for i in range(len(A)):
        tmp = 0
        for j in range(len(A[i])):
            tmp += A[i][j]*y[j]
        if round(b[i]) == round(tmp):
            res.append(i+1)
    return res

print("(a, b) - zrób a 0.5m papierów, zrób b 1.4m papierów")
s = solve_(A, res, b)

for i in range(len(s)):
    print(conf[s[i]-1])
