import math
import numpy as np

def print_(m):
    for i in range(len(m)):
        print(m[i])

def calcB(M, n, k, vec):
    b = []
    for i in range(n-k):
        tmpB = 1
        for j in range(n):
            tmpB *= M[i][j]
        for q in range(k):
            tmpB *= vec[q][0]
        b.append(math.log10(tmpB))
    return b

def genA(n, k):
    A = []
    for i in range(n-k):
        row = []
        for j in range(n-k):
            if i == j:
                row.append(n-1)
            else:
                row.append(-1)
        A.append(row)
    return A

def calcW(A, b, vec):
    W = np.dot(np.linalg.inv(A), b)
    for i in range(len(W)):
        tmp = 10**W[i]
        W[i] = tmp
    W = np.append(W, vec)
    return W

def geometric(M, n, k, vec):
    b = calcB(M, n, k, vec)
    print("b")
    print_(b)
    A = genA(n, k)
    print("A")
    print_(A)
    W = calcW(A, b, vec)
    print("W")
    print_(W)

A=[[1,2/3,2,5/2,5/3,5],[
3/2,1,3,10/3,3,9],[
1/2,1/3,1,4/3,7/8,5/2],[
2/5,3/10,3/4,1,5/6,12/5],[
3/5,1/3,8/7,6/5,1,3],[
1/5,1/9,2/5,5/12,1/3,1]]

B=[[1,2/5,3,7/3,1/2,1],[
5/2,1,4/7,5/8,1/3,3],[
1/3,7/4,1,1/2,2,1/2],[
3/7,8/5,2,1,4,2],[
2,3,1/2,1/4,1,1/2],[
1,1/3,2,1/2,2,1]]

C=[[1,17/4,17/20,8/5,23/6,8/3],[
4/17,1,1/5,2/5,9/10,2/3],[
20/17,5,1,21/10,51/10,10/3],[
5/8,5/2,10/21,1,5/2,11/6],[
6/23,10/9,10/51,2/5,1,19/30],[
3/8,3/2,3/10,6/11,30/19,1]]

print("#### średnia geometryczna")
print("zad A")
geometric(A, 6, 2, [[3], [1]])
print("zad B")
geometric(B, 6, 3, [[2], [1/2], [1]])
print("zad C")

C = np.array(C)
C[:, [1, 4]] = C[:, [4, 1]]
C[:, [3, 5]] = C[:, [5, 3]]
C[1], C[4] = C[4], C[1]
C[3], C[5] = C[5], C[3]

geometric(C, 6, 2, [[2], [5]])
