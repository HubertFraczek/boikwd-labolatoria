import numpy as np

G = np.array([
	[20, -150, -250],
	[150, -80, -100],
	[250, 100, 40]
])

def minimax(X):
	mins = []
	maxes = []
	for i in range(len(X)):
		mins.append((min(X[i]), i))
		maxes.append((max(X[:,i]), i))
	return ("A", max(mins)[-1]), ("B", min(maxes)[-1])

def minimax_seq(s1, s2, s3, p1_coins, p2_coins, p1_picks, p2_picks, p1_prev, p2_prev):
	pass


print(G)
print(minimax(G))

