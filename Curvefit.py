import numpy as ny 
import matplotlib.pyplot as pt
from scipy.optimize import curve_fit
for I in range(1,10): # Defining a loop so that we don't need to codes for different types of polynomials
	def f(t, a, b, c, d, e, f, g, h, i, j): # Defining the function for multiple polynomials again to evade typing long codes
		if I==1: # Algebraic Equation of first Degree or Linear Equation
			return a*t**1 + b*t**0 +   0*(c*t**7 + d*t**6 + e*t**5 + f*t**4 + g*t**3 + h*t**2 + i*t**1 + j*t**0)
		if I==2: # Algebraic Equation of Second Degree or Quadratic Equation
			return a*t**2 + b*t**1 + c*t**0 +   0*(d*t**6 + e*t**5 + f*t**4 + g*t**3 + h*t**2 + i*t**1 + j*t**0)
		if I==3: # Algebraic Equation of Third Degree or Cubic Equation
			return a*t**3 + b*t**2 + c*t**1 + d*t**0 +   0*(e*t**5 + f*t**4 + g*t**3 + h*t**2 + i*t**1 + j*t**0)
		if I==4: # Algebraic Equation of Fourth Degree
			return a*t**4 + b*t**3 + c*t**2 + d*t**1 + e*t**0 +   0*(f*t**4 + g*t**3 + h*t**2 + i*t**1 + j*t**0)
		if I==5: # Algebraic Equation of Fifth Degree 
			return a*t**5 + b*t**4 + c*t**3 + d*t**2 + e*t**1 + f*t**0 +   0*(g*t**3 + h*t**2 + i*t**1 + j*t**0)
		if I==6: # Algebraic Equation of Sixth Degree
			return a*t**6 + b*t**5 + c*t**4 + d*t**3 + e*t**2 + f*t**1 + g*t**0 +   0*(h*t**2 + i*t**1 + j*t**0)
		if I==7: # Algebraic Equation of Seventh Degree
			return a*t**7 + b*t**6 + c*t**5 + d*t**4 + e*t**3 + f*t**2 + g*t**1 + h*t**0 +   0*(i*t**1 + j*t**0)			
		if I==8: # Algebraic Equation of Eighth Degree
			return a*t**8 + b*t**7 + c*t**6 + d*t**5 + e*t**4 + f*t**3 + g*t**2 + h*t**1 + i*t**0 +   0*(j*t**0)
		if I==9: # Algebraic Equation of Ninth Degree
			return a*t**9 + b*t**8 + c*t**7 + d*t**6 + e*t**5 + f*t**4 + g*t**3 + h*t**2 + i*t**1 + j*t**0	

	def rf(): # Defining the function for getting data from the file given to us
		T = [] # Null array for storing values of Temperatures given in datafile (in K)
		cp = [] # Null array for storing values of Cp
		for line in open('data','r'): # A loop to read every line one at a time from the data file
			v = line.split(',') # Spliting the line from wherever there is (,)
			T.append(float(v[0])) # Storing the value of first element in array formed by spliting the line in a Null array
			cp.append(float(v[1])) # Storing the value of second element in array formed by spliting the line in a Null array
		return [T, cp] # Returing the values in the form of an array

	T , cp = rf() # Storing the values came from the function which was defined to get the data
	P, C = curve_fit(f,T,cp) # Key to fit a curve of function f(Defined earlier) with x = T and y = cp
	fit = f(ny.array(T), *P) # Using a single variable to store the value of function f(Defined earlier) where t is replaced by array of T and all other arguments is passed by P
	# Plotting the Graph
	tt = 'Algebraic Equation of ' + str(I) + ' Degree'
	pt.plot(T,cp, color='Blue', label='Actual')
	pt.plot(T, fit, color='Red', label='Curve fit')
	pt.title(tt)
	pt.legend()
	pt.xlabel('Temperature (in K)')
	pt.ylabel('Cp')
	pt.show()