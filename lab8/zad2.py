import numpy as np
from scipy.optimize import linprog

A = np.array([[-0.5, -0.4],
    [-0.4, -0.2],
    [-0.4, 0],
    [-0.2, -0.5]])

c = [2000, 2800]

b = np.array([-10, -14, -8, -11]) 

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
        if b[i] == tmp:
            res.append(i+1)
    return res

print("kup produkty numer:")
print(solve_(A, res, b))    
