from ahp import ahp, ahp2
import numpy as np

# jako kryterium ceny biore odwrotnosc z iloczynu ceny i spalania paliwa
# jako kryterium pojemnosci biore iloczyn pojemnosci bagaznika i ilosc pasazerow
s1 = [1/(68200 * 8.91), 4/5, 450 * 5] 
s2 = [1/(39900 * 11.2), 3.5/5, 415 * 5]
s3 = [1/(87394 * 5.81), 4.5/5, 430 * 4]

cars = [s1, s2, s3]

tmp = np.array(np.zeros((3,3)))

for i in range(3):
	for j in range(3):
		tmp[i][j] = cars[i][0] / cars[j][0]
c1 = np.matrix([tmp[0],tmp[1],tmp[2]])

for i in range(3):
	for j in range(3):
		tmp[i][j] = cars[i][1] / cars[j][1]
c2 = np.matrix([tmp[0],tmp[1],tmp[2]])

for i in range(3):
	for j in range(3):
		tmp[i][j] = cars[i][2] / cars[j][2]
c3 = np.matrix([tmp[0],tmp[1],tmp[2]])

c4 = np.matrix([
	[1, 4, 7],
	[1/4, 1, 5],
	[1/7, 1/5, 1]
])

c = [c1, c2, c3, c4]

k = ahp(c)

res = np.array([
	k[0], k[1], k[2]
])

ahp2(res, k, 3)
