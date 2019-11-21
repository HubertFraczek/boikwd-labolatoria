import scipy.optimize as scipy
import numpy as np

A = [[-4, -2, -7, -4], [-6, -4, -7, -1], [-1, -1, -4, -8], [-4, -7, 0, -4]]
b = [-1, -1, -1, -1]
c = [1, 1, 1, 1]

res = scipy.linprog(c, A, b).x
f = res[0] + res[1] + res[2] + res[3]
V = 1 / f

print("A")
print("res =", res)
print("x1 + x2 + x3 + x4 =", f)
print("Wartosc gry =", V - 4)

print("prawdopodobienstwa:")
print("A1,2 =", V * res[0])
print("A1,3 =", V * res[1])
print("A2,3 =", V * res[2])
print("A2,4 =", V * res[3])


A = [[4, 6, 1, 4], [2, 4, 1, 7], [7, 7, 4, 0], [4, 1, 8, 4]]
b = [1, 1, 1, 1]
c = [-1, -1, -1, -1]

res = scipy.linprog(c, A, b).x
f = res[0] + res[1] + res[2] + res[3]
V = 1 / f

print()
print("B")
print("res =", res)
print("x1 + x2 + x3 + x4 =", f)
print("Wartość gry =", V - 4)

print("prawdopodobienstwa:")
print("B1,2 =", V * res[0])
print("B1,3 =", V * res[1])
print("B2,3 =", V * res[2])
print("B2,4 =", V * res[3])
