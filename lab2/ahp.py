import numpy as np
from numpy import linalg as LA

def ahp(c):
	# oblicznie wartosci wlasnych i wektorow wlasnych
	v = []
	w = []
	for i in c:
		tmpW, tmpV = LA.eig(i)
		w.append(tmpW)
		v.append(tmpV)

	# wybieranie kolumny odpowiadajacej najwiekszej wartosci wlasnej
	k = []
	for i in range(len(v)):
		tmpK = v[i][:,np.argmax(w[i])]
		k.append(tmpK)

	# normalizacja
	for i in k:
		normalize(i)

	return k

def ahp2(res, k, n):
	resTr = np.transpose(res)
	result = np.matmul(resTr, k[-1])

	print(resTr)
	print()
	print(k[-1])
	print()
	print(result)

	f = open("zad" + str(n) + ".txt", "w+")
	for i in k:
		f.write("\n")
		f.write(str(i))
		f.write("\n")
	f.write("\n\n")
	f.write(str(result))
	f.close()

def normalize(vec):
	s = sum(vec)
	for i in vec:
		i /= s
