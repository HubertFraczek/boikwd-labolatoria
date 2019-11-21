import scipy.optimize as scipy
import numpy as np

A = [[0, -5], [-10, -1], [-4, -2]]
b = [-1, -1, -1]
c = [1, 1]

res = scipy.linprog(c, A, b).x
f = res[0] + res[1]
V = 1 / f

print("A")
print("res =", res)
print("x1 + x2 =", f)
print("Wartosc gry", V - 2)
print("A1 =", V * res[0])
print("A2 =", V * res[1])


A = [[0, 10, 4], [5, 1, 2]]
b = [1, 1]
c = [-1, -1, -1]

res = scipy.linprog(c, A, b).x
f = res[0] + res[1] + res[2]
V = 1 / f

print()
print("B")
print("res =", res)
print("x1 + x2 + x3 =", f)
print("Wartosc gry =", V - 2)
print("B1 =", V * res[0])
print("B2 =", V * res[1])
print("B3 =", V * res[2])