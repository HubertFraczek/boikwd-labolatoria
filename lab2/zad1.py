import numpy as np
from numpy import linalg as LA

def normalize(vec):
	s = sum(vec)
	for i in vec:
		i /= s
	return vec

c1 = np.matrix([
	[1, 1/7, 1/5],
	[7, 1, 3],
	[5, 1/3, 1]
])

c2 = np.matrix([
	[1, 5, 9],
	[1/5, 1, 4],
	[1/9, 1/4, 1]
])

c3 = np.matrix([
	[1, 4, 1/5],
	[1/4, 1, 1/9],
	[5, 9, 1]
])

c4 = np.matrix([
	[1, 9, 4],
	[1/9, 1, 1/4],
	[1/4, 4, 1]
])

c5 = np.matrix([
	[1, 1, 1],
	[1, 1, 1],
	[1, 1, 1]
])

c6 = np.matrix([
	[1, 6, 4],
	[1/6, 1, 1/3],
	[1/4, 3, 1]
])

c7 = np.matrix([
	[1, 9, 6],
	[1/9, 1, 1/3],
	[1/6, 3, 1]
])

c8 = np.matrix([
	[1, 1/2, 1/2],
	[2, 1, 1],
	[2, 1, 1]
])

w1, v1 = LA.eig(c1)
w2, v2 = LA.eig(c2)
w3, v3 = LA.eig(c3)
w4, v4 = LA.eig(c4)
w5, v5 = LA.eig(c5)
w6, v6 = LA.eig(c6)
w7, v7 = LA.eig(c7)
w8, v8 = LA.eig(c8)

k1 = v1[:,np.argmax(w1)]
k2 = v2[:,np.argmax(w2)]
k3 = v3[:,np.argmax(w3)]
k4 = v4[:,np.argmax(w4)]
k5 = v5[:,np.argmax(w5)]
k6 = v6[:,np.argmax(w6)]
k7 = v7[:,np.argmax(w7)]
k8 = v8[:,np.argmax(w8)]

normalize(k1)
normalize(k2)
normalize(k3)
normalize(k4)
normalize(k5)
normalize(k6)
normalize(k7)
normalize(k8)

c9 = np.matrix([
	[1, 4, 7, 5, 8, 6, 6, 2],
	[1/4, 1, 5, 3, 7, 6, 6, 1/3],
	[1/7, 1/5, 1, 1/3, 5, 3, 3, 1/5],
	[1/5, 1/3, 3, 1, 6, 3, 4, 1/2],
	[1/8, 1/7, 1/5, 1/6, 1, 1/3, 1/4, 1/7],
	[1/6, 1/6, 1/3, 1/3, 3, 1, 1/2, 1/5],
	[1/6, 1/6, 1/3, 1/4, 4, 2, 1, 1/5],
	[1/2, 3, 5, 2, 7, 5, 5, 1]
])

w9, v9 = LA.eig(c9)
k9 = v9[:,np.argmax(w9)]
normalize(k9)

res = np.array([
	k1, k2, k3, k4, k5, k6, k7, k8
])

print(np.transpose(res))
print()
print(k9)
print()
print(np.matmul(np.transpose(res), k9))
