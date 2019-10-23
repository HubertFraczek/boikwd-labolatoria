import math
import numpy as np

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

A=[[1,2/3,2,5/2,5/3,5],[
3/2,1,3,10/3,3,9],[
1/2,1/3,1,4/3,7/8,5/2],[
2/5,3/10,3/4,1,5/6,12/5],[
3/5,1/3,8/7,6/5,1,3],[
1/5,1/9,2/5,5/12,1/3,1]]

n = 6
k = 2
v = 1 - ((1 + math.sqrt(4 * (n - 1) * (n - k - 2))) / (2 * (n - 1)))
print(koczkodaj(A) < v)

def genA(A, n, k):
    A1 = []
    for i in range(n-k):
        A1.append(A[i][0:(n-k)])

    A2 = []
    for i in range(n-k):
        A2.append(A[i][n-k:n])
    
    return A1, A2

def mulA(A, n):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i != j:
                A[i][j] *= (-1/(n-1))
    return A

def mulB(A, n, wk):
    for i in range(len(A)):
        for j in range(len(A[0])):
                A[i][j] *= (1/(n-1))
    return np.dot(A, wk)

def print_(m):
    for i in range(len(m)):
        print(m[i])

A1, A2 = genA(A, n, k)
print("A1")
print_( A1)
print("A2")
print_(A2)

a = mulA(A1, n)
b = mulB(A2, n, [[3], [1]])

print()
print_(a)
print()
print_(b)

W = np.dot(np.linalg.inv(a), b)
W = np.append(W, [[3], [1]])
print()
print_(W)


