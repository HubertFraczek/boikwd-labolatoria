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

# B
B=[[1,2/5,3,7/3,1/2,1],[
5/2,1,4/7,5/8,1/3,3],[
1/3,7/4,1,1/2,2,1/2],[
3/7,8/5,2,1,4,2],[
2,3,1/2,1/4,1,1/2],[
1,1/3,2,1/2,2,1]]
n = 6
k = 3
v = 1 - ((1 + math.sqrt(4 * (n - 1) * (n - k - 2))) / (2 * (n - 1)))

A1, A2 = genA(B, n, k)
print("#########3 B")
print("A1")
print_( A1)
print("A2")
print_(A2)

a = mulA(A1, n)
b = mulB(A2, n, [[2], [1/2], [1]])

print()
print_(a)
print()
print_(b)

W = np.dot(np.linalg.inv(a), b)
W = np.append(W, [[2], [1/2], [1]])
print()
print_(W)

# C
C=[[1,17/4,17/20,8/5,23/6,8/3],[
4/17,1,1/5,2/5,9/10,2/3],[
20/17,5,1,21/10,51/10,10/3],[
5/8,5/2,10/21,1,5/2,11/6],[
6/23,10/9,10/51,2/5,1,19/30],[
3/8,3/2,3/10,6/11,30/19,1]]
n = 6
k = 2
v = 1 - ((1 + math.sqrt(4 * (n - 1) * (n - k - 2))) / (2 * (n - 1)))

C[2], C[4] = C[4], C[2]
C[4], C[5] = C[5], C[4]

A1, A2 = genA(C, n, k)
print("#########3 C")
print("A1")
print_( A1)
print("A2")
print_(A2)

a = mulA(A1, n)
b = mulB(A2, n, [[2], [5]])

print()
print_(a)
print()
print_(b)

W = np.dot(np.linalg.inv(a), b)
W = np.append(W, [[2], [5]])
print()
print_(W)



