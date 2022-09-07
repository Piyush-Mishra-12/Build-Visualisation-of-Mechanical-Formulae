# Importing Important modules
import math
import matplotlib.pyplot as plt
import numpy as np

# Taking the name of file as input from the user
f = input('Please Enter the name of file where data is stored \n  (File name here is engine_data.out)  \n')
print('\nNow, We can choose any Two Parameter From Below list to Construct the Plot between those to Parameters \n(Enter a Number Corresponding to Parameter 1 to 17)')
lc = 1
for l in open('engine_data.out'):
	if lc ==3:
		p = str.split(l)
		for c in range(1,len(p)):
			print(c, '-', p[c])
	lc = lc + 1

y = 2#int(input("Enter the Parameter for Y-axis : "))
x = 8#int(input("Enter the Parameter for X-axis : "))
P = []
U = []
X = []
Y = []
lc = 1
for l in open('engine_data.out'):
	if '#' not in l:
		X.append(float(l.split()[x-1]))
		Y.append(float(l.split()[y-1]))
	else:
		if lc ==3:
			p = l.split()
			for c in range(1,len(p)):
				P.append(p[c])		
		if lc ==4:
			u = l.split()
			for c in range(1,len(u)):
				U.append(u[c])
		lc = lc + 1
print(P)
filename = P[y-1] + '  vs  ' + P[x-1] + '.png'
print(filename)
plt.figure()
plt.plot(X,Y)
plt.xlabel(P[x-1] + U[x-1])
plt.ylabel(P[y-1] + U[y-1])
plt.title(P[y-1] + '  vs  ' + P[x-1])
plt.savefig(filename)
plt.sho
