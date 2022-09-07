# Importing Important Module
import numpy as np
import matplotlib.pyplot as pt
# Inputs
B = 0.5 ## It is related to width of ice wedge
r = 40 # Size of the Air Cushion (in ft)
s = 21600 # Tensile Strength of ice (in psf) <150 psi X 144 = 21600psf>
h = [0.6, 1.2, 1.8, 2.4, 3.0, 3.6, 4.2] # Array of thickness of the ice field (in ft)
a = 1.2 # Relaxation factor assumed

def f(p, h, r, B, s): # Defining the function that need to be varied over time
    return pow(p,3)*(1-pow(B,2)) + pow(p,2)*(0.4*h*pow(B,2)-(s*pow(h,2)/pow(r,2))) + p*(pow(s,2)*pow(h,4)/(3*pow(r,4))) - pow((s*pow(h,2)/(3*pow(r,2))),3)
def F(p, h, r, B, s): # Defining the derivative of function that need to be varied over time
	return 3*pow(p,2)*(1-pow(B,2)) + p*2*(0.4*h*pow(B,2)-(s*pow(h,2)/pow(r,2))) + (pow(s,2)*pow(h,4)/(3*pow(r,4)))

# Ploting for Cushion Pressure vs Ice Field Thickness
P = []  # Null array for storing values of Pressure in array'''
tol = 1e-4 # Tolerance upto which calculation need to be same so that our iteration can be stopped
for i in h: # Defining h in loop so that we can get the results for all the stated values of h (Thickness of the ice field)
	pg = 90 # Assuming initial pressure value <This is supposed to be done inside the for loop bcuz we want pg to be first vlue for every value of h>
	ct = 1 # Initializing the counter variable which will represent the number of iterations <for every value of h>
	while (abs(f(pg, i, r, B, s)) > tol): # Defining upto which value we need to continue iterating
		pg = pg - a*(f(pg, i, r, B, s) / F(pg, i, r, B, s)) # Value of pg that keeps changing until we achive a constant results
		ct = ct + 1 # This mainly to tell us that how many times we have iterated to get to the particular results
	print('Cushion Pressure at h =',i,'feet is',"%.4f" % pg,'psf', 'by doing',ct, 'Number of iterations')
	P.append(pg) # Storing the value of pg in Null array for ploting
# Plotting Graph
pt.plot(h, P, marker='*')
pt.title('Cushion Pressure vs Ice Field Thickness')
pt.xlabel('Thickness of Ice Field (feet)')
pt.ylabel('Cushion Pressure (pound per square feet)')
pt.show()

# Ploting for Iterations vs Relaxation Factor
A = np.linspace(0.2, 1.99, 100) # Creating an array of number for which Relaxation Factor is defined <For more than 2 we are getting 2 values of pg so it can never be same and hence niether the while loop will stop nor our plot will appear >
h1 = 0.6 # Thickness of the ice field (in ft)
CT = [] # Null array for storing the number of iterations in future
for j in A: # Defining A in loop so that we can get the results for all the stated values of A (Relaxation Factor)
	pg = 90 # Assuming initial pressure value <This is supposed to be done inside the for loop bcuz we want pg to be first vlue for every value of h>
	ct = 1 # Initializing the counter variable which will represent the number of iterations <for every value of h>
	while ((abs(f(pg, h1, r, B, s))) > tol): # Defining upto which value we need to continue iterating
		pg = pg - j*(f(pg, h1, r, B, s) / F(pg, h1, r, B, s)) # Value of pg that keeps changing until we achive a constant results
		ct = ct + 1# This mainly to tell us that how many times we have iterated to get to the particular results
	CT.append(ct) # Storing the value of ct in Null array for ploting
m= CT.index(min(CT)) # For finding Minimum value of iterations
O= A[m] # For finding Optimum value of Relaxation Factor
print("Optimum value of Relaxation Factor is","%.4f" % O) 
print("Min Value Iteration=",min(CT))
# Ploting Graph
pt.plot(A, CT)
pt.title('Iterations vs Relaxation Factor')
pt.xlabel('Relaxation Factor')
pt.ylabel('Number of Iterations')
pt.show()