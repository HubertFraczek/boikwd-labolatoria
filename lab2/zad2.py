import numpy as np
from numpy import linalg as LA

def normalize(vec):
	s = sum(vec)
	for i in vec:
		i /= s

h1 = [210,20,20,1]
h2 = [150,20,30,2]
h3 = [230,30,12,1]
h4 = [250,25,8,2]

hotels = [h1, h2, h3, h4]

tmp = np.array(np.zeros((4,4)))

# cena
for i in range(4):
	for j in range(4):
		tmp[i][j] = hotels[i][0] / hotels[j][0]
c1 = np.matrix([tmp[0],tmp[1],tmp[2],tmp[3]])

# wyzywienie
for i in range(4):
	for j in range(4):
		tmp[i][j] = hotels[i][1] / hotels[j][1]
c2 = np.matrix([tmp[0],tmp[1],tmp[2],tmp[3]])

# odleglosc
for i in range(4):
	for j in range(4):
		tmp[i][j] = hotels[i][2] / hotels[j][2]
c3 = np.matrix([tmp[0],tmp[1],tmp[2],tmp[3]])

# parking
for i in range(4):
	for j in range(4):
		tmp[i][j] = hotels[i][3] / hotels[j][3]
c4 = np.matrix([tmp[0],tmp[1],tmp[2],tmp[3]])

w1, v1 = LA.eig(c1)
w2, v2 = LA.eig(c2)
w3, v3 = LA.eig(c3)
w4, v4 = LA.eig(c4)


k1 = v1[:,np.argmax(w1)]
k2 = v2[:,np.argmax(w2)]
k3 = v3[:,np.argmax(w3)]
k4 = v4[:,np.argmax(w4)]

normalize(k1)
normalize(k2)
normalize(k3)
normalize(k4)

c5 = np.matrix([
	[1,5,3,4],
    [1/5,1,4,1],
    [1/3,1/4,1,2],
    [1/4,1,1/2,1]
])

w5, v5 = LA.eig(c5)
k5 = v5[:,np.argmax(w5)]
normalize(k5)

res = np.array([
	k1, k2, k3, k4
])

print(np.transpose(res))
print()
print(k5)
print()
print(np.matmul(np.transpose(res), k5))
