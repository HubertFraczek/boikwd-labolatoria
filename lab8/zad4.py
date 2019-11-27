import numpy as np
from scipy.optimize import linprog

conf = [(2, 1, 0), (1, 2, 0), (1, 1, 2), (0, 3, 1), (0, 2, 2), (0, 1, 4), (0, 0, 6)]

A = np.array([[-2, -1, 0],
    [-1, -2, 0],
    [-1, -1, -2],
    [0, -3, -1],
    [0, -2, -2],
    [0, -1, -4],
    [0, 0, -6]])

c = [12000, 24000, 27000]

b = np.array([0, -3, -1, -1, -4, -2, 0]) 

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

print("(a, b, c) - zrób a 11cm gwoździ, zrób b 8cm gwoździ, zrób c 5cm gwoździ")
s = solve_(A, res, b)

for i in range(len(s)):
    print(conf[s[i]-1])
