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
                    return True
        return False
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
    n = len(M)
    if (n % 2 == 0):
        return (1 - counter/((n**3 - 4*n) / 24))
    else:
        return (1 - counter/((n**3 - n) / 24))

def uogolnionyKendall(M):
    n = len(M)
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if M[i][j] == M[j][k] and M[j][k] == M[k][i] and M[k][i] != 0:
                    counter += 1
                if M[i][j] == 1 or M[i][j] == -1:
                    if M[j][k] == 0 and M[k][i] == 0:
                        counter += 1
                elif M[j][k] == 1 or M[j][k] == -1:
                    if M[i][j] == 0 and M[k][i] == 0:
                        counter += 1
                elif M[k][i] == 1 or M[k][i] == -1:
                    if M[i][j] == 0 and M[j][k] == 0:
                        counter += 1
                if M[i][j] == 0:
                    if M[j][k] == M[k][i] and M[k][i] != 0:
                        counter += 1
                elif M[j][k] == 0:
                    if M[k][i] == M[i][j] and M[i][j] != 0:
                        counter += 1
                elif M[k][i] == 0:
                    if M[i][j] == M[j][k] and M[i][j] != 0:
                        counter += 1
    if n % 4 == 0:
        y = (13 * n**3 - 24 * n * n - 16 * n) / 96
    elif n % 4 == 1:
        y = (13 * n**3 - 24 * n * n - 19 * n + 30) / 96
    elif n % 4 == 2:
        y = (13 * n**3 - 24 * n * n - 4 * n) / 96
    else:
        y = (13 * n**3 - 24 * n * n - 19 * n + 18) / 96

    return 1 - (counter / y)

At = turniejowa(A)
Bt = turniejowa(B)
Ct = turniejowa(C)
print("Turniejowa A - ", isTurniejowa(At))
print("Turniejowa B - ", isTurniejowa(Bt))
print("Turniejowa C - ", isTurniejowa(Ct))
print("Turniejowa D - ", isTurniejowa(D))
print("Turniejowa E - ", isTurniejowa(E))
print("Turniejowa F - ", isTurniejowa(F))
print("Mozliwe remisy A - ", isUogolniona(At))
print("Mozliwe remisy B - ", isUogolniona(Bt))
print("Mozliwe remisy C - ", isUogolniona(Ct))
print("Mozliwe remisy E - ", isUogolniona(E))
print("Mozliwe remisy F - ", isUogolniona(F))
print("Kendall A - ", kendall(At))
print("Kendall F - ", kendall(F))
print("Uogolniony Kendall B - ", uogolnionyKendall(B))
print("Uogolniony Kendall C - ", uogolnionyKendall(C))
print("Uogolniony Kendall E - ", uogolnionyKendall(E))
