from scipy.optimize import linprog

A = [[2, 1, -9000], [1, 1, -5500], [1, 2.5, -10000], [-1, 0, 100], [0, -1, 100], [36.8, 65.7, 1], [-36.8, -65.7, -1]]
b = [0,0,0,0,0,1,-1]
c = [150, 130, 0]
bounds = [(0, None),(0, None),(0, None)]
maxi = True

if maxi:
    res = linprog([i * -1 for i in c], A, b, bounds = bounds, options = {"disp": False}).x
else:
    res = linprog(c, A, b, bounds = bounds, options = {"disp": False}).x

print(res)
 
x1 = res[0]/res[2]
print("A:", x1)
 
x2 = res[1]/res[2]
print("B:", x2)