import numpy as np
import math

def normalize(v):
	s = sum(v)
	newV = []
	for i in v:
		newV.append(i / s)
	return newV

A = [[1, 7, 3], [1 / 7, 1, 2], [1 / 3, 1 / 2, 1]]
B = [[1, 1 / 5, 7, 1], [5, 1, 1 / 2, 2], [1 / 7, 2, 1, 3], [1, 1 / 2, 1 / 3, 1]]
C = [[1, 2, 5, 1, 7], [1 / 2, 1, 3, 1 / 2, 5], [1 / 5, 1 / 3, 1, 1 / 5, 2], [1, 2, 5, 1, 7],
     [1 / 7, 1 / 5, 1 / 2, 1 / 7, 1]]

# indeks Saaty'ego
maxEigA = np.amax(np.linalg.eigvals(A))
maxEigB = np.amax(np.linalg.eigvals(B))
maxEigC = np.amax(np.linalg.eigvals(C))

saatyA = (maxEigA - len(A)) / (len(A) - 1)
saatyB = (maxEigB - len(B))/(len(B) - 1)
saatyC = (maxEigC - len(C))/(len(C) - 1)

print("saaty")
print(saatyA)
print(saatyB)
print(saatyC)

# indeks geometryczny # cos sie wyniki nie zgadzaja
# tA = 2 / ((len(A) - 1) * (len(A) - 2))
# tB = 2 / ((len(B) - 1) * (len(B) - 2))
# tC = 2 / ((len(C) - 1) * (len(C) - 2))

# def avgCol(j, m):
# 	tmp = 1
# 	for i in range(len(m)):
# 		tmp *= m[i][j]
# 	res = math.pow(tmp, 1 / len(m))	
# 	return res

# def avgRow(i, m):
# 	tmp = 1
# 	for j in range(len(m)):
# 		tmp *= m[i][j]
# 	res = math.pow(tmp, 1 / len(m))	
# 	return res

# def geo(m):
# 	res = 0
# 	for i in range(len(m)):
# 		tmp = 0
# 		for j in range(i + 1, len(m)):
# 			tmp += math.pow(math.log(m[i][j] * (avgCol(j, m) / avgRow(i, m)), 10), 2)
# 		res += tmp
# 	return res

# print("geo")
# print(geo(A))
# print(geo(B))
# print(geo(B))

#indeks Koczkodaja
def koczkodaj(m):
	res = 0
	for i in range(len(m)):
	    for j in range(len(m)):
	        for k in range(len(m)):
	            l = min(abs(1 - (m[i][k] * m[k][j]) / m[i][j]), 
	            	abs(1 - m[i][j] / (m[i][k] * m[k][j])))
	            if l > res:
	                res = l
	return res

print("koczkodaj")
print(koczkodaj(A))
print(koczkodaj(B))
print(koczkodaj(C))
