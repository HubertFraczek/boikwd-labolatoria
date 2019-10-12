from ahp import ahp, ahp2
import numpy as np

h1 = [210, 20, 20, 1]
h2 = [150, 20, 30, 2]
h3 = [230, 30, 12, 1]
h4 = [250, 25, 8, 2]

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

c5 = np.matrix([
	[1,5,3,4],
    [1/5,1,4,1],
    [1/3,1/4,1,2],
    [1/4,1,1/2,1]
])

c = [c1, c2, c3, c4, c5]

k = ahp(c)

res = np.array([
	k[0], k[1], k[2], k[3]
])

ahp2(res, k, 2)
