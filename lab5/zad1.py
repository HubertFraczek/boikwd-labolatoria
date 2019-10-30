import numpy as np

A=np.array([[1,2/3,2,5/2,5/3,5],[3/2,1,3,10/3,3,9],[1/2,1/3,1,4/3,7/8,5/2],[2/5,3/10,3/4,1,5/6,12/5],[3/5,1/3,8/7,6/5,1,3],[1/5,1/9,2/5,5/12,1/3,1]])

B=np.array([[1,2/5,3,7/3,1/2,1,2],[5/2,1,4/7,1,1,3,2/3],[1/3,7/4,1,1/2,2,1/2,1],[3/7,1,2,1,4,2,6],[2,1,1/2,1/4,1,1/2,3/4],[1,1/3,2,1/2,2,1,5/8],[1/2,3/2,1,1/6,4/3,8/5,1]])

C=np.array([[1,2/3,2/15,1,8,12/5,1,1/2],[3/2,1,1,2,1,2/3,1/6,1],[15/2,1,1,5/2,7/8,2,1,1/5],[1,1/2,2/5,1,4/3,1,2/7,1],[1/8,1,8/7,3/4,1,1/5,2/7,1],[5/12,3/2,1/2,1,5,1,3,2],[1,6,1,7/2,7/2,1/3,1,3/11],[2,1,5,1,1,1/2,11/3,1]])

D=np.array([[0,1,1,-1,-1,1,-1],[-1,0,0,1,1,-1,0],[-1,0,0,0,1,1,-1],[1,-1,0,0,1,0,1],[1,0,-1,-1,0,1,-1],[-1,1,-1,1,-1,0,0],[1,0,1,-1,1,0,0]])

E=np.array([[0,1,0,0,-1],[-1,0,0,0,1],[0,0,0,1,0],[0,0,-1,0,0],[1,-1,0,0,0]])

F=np.array([[0,-1,1,-1,1,-1,1,-1,1],[1,0,1,1,1,-1,-1,-1,-1],[-1,-1,0,-1,1,-1,1,1,1],[1,-1,1,0,-1,1,-1,1,-1],[-1,-1,-1,1,0,-1,1,1,1],[1,1,1,-1,1,0,-1,-1,-1],[-1,1,-1,1,-1,1,0,1,-1],[1,1,-1,-1,-1,1,-1,0,1],[-1,1,-1,1,-1,1,1,-1,0]])

def turniejowa(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == j:
                M[i][j] = 0
            else:
                if M[i][j] == 1:
                    M[i][j] = 0
                elif M[i][j] > 1:
                    M[i][j] = 1
                else:
                    M[i][j] = -1
    return M

def isUogolniona(M):
    if isTurniejowa(M):
        for i in range(len(M)):
            for j in range(len(M[0])):
                if i != j and M[i][j] == 0:
                    return False
        return True
    return False

def isTurniejowa(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if (M[i][j] != -M[j][i]):
                return False
    return True

def kendall(M):
    counter = 0
    for i in range(len(M)):
        for j in range(i+1, len(M)):
            for k in range(j+1, len(M)):
                if M[i][j] == M[j][k] and M[j][k] == M[k][i] and M[i][j] == M[k][i]:
                    counter += 1
    return counter

def indeksKendalla(M, c):
    n = len(M)
    if (n % 2 == 0):
        return (1 - c/((n**3 - 4*n) / 24))
    else:
        return (1 - c/((n**3 - n) / 24))

print("A")
print(A)
At = turniejowa(A)
Bt = turniejowa(B)
Ct = turniejowa(C)
print(At)
print(isTurniejowa(At))
print(isTurniejowa(Bt))
print(isTurniejowa(Ct))
print(isUogolniona(At))
print(isUogolniona(Bt))
print(isUogolniona(Ct))
print(isUogolniona(D))
print(isUogolniona(E))
print(isUogolniona(F))
print(indeksKendalla(At, kendall(At)))

