import math
import matplotlib.pyplot as pt
import numpy as ny
# Given Inputs
P1 = 100 # in kPa <Initial Pressure is below always below the atmospheric Pressure>
T1 = 300 # in K
T3 = 1800 # in K
r = 10 # Compression Ratio of petrol = V1/V2
y = 1.4 # Value of gamma in air
b = 0.05 # Dia of cyclender in m
s = 0.2 # Stroke of cylinder in m
Pc = [] # Defining an Null Array for Compression Pressure
Pe = [] # Defining an Null Array for Expansion Pressure
V = [] # Defining an Array for Volume <It's main use is while ploting as both x and y plots need to of same dimensions>
for t in ny.linspace(0,math.pi,180): # t here means angle Theta <We are creating an array for value for theta in for loop as for every value theta swept volume changes>
# Volume Calculation 	
	Vs = math.pi/4*b*b * (  s/2 + (s/2 * math.cos(t))  ) # Swept Volume in m^3 at different position of crank radius
	Vc = math.pi/4*b*b * (  s/2 + (s/2 * math.cos(0))  ) / (r-1) # Clearance Volume in m^3 <here swept volume should be max>
	v = Vc + Vs # Volume of different positions of theta as swept volume changes
	V1 = math.pi/4*b*b * (  s/2 + (s/2 * math.cos(0))  ) + Vc
	V2 = math.pi/4*b*b * (  s/2 + (s/2 * math.cos(math.pi))  ) + Vc 
	V3 = V2
	V4 = V1
# Pressure Calculation 	
	P2 = P1*pow(r,y)
	m = P1*V1/(0.287*300) # mass of air in kg
	P3 = m*0.287*T3/V3 # 0.287 kJ/kgK is the value of R in PV=mRT 
	P4 = P3/pow(r,y)	# (V3/V4) = (V2/V1) = (1/r)
	pc = P1*pow(V1,y)/pow(v,y) # Compression Pressure of different positions of theta as swept volume changes in Compression process
	pe = P3*pow(V3,y)/pow(v,y) # Expansion Pressure of different positions of theta as swept volume changes in Expansion process
	Pc.append(pc)
	Pe.append(pe)
	V.append(v)
# Printing Some Important Values
print('V1 =',V1,'m^3')
print('V2 =',V2,'m^3')
print('Mass =',m,'kg')
print('P1 =',P1,'kPa')
print('P2 =',P2,'kPa')
print('P3 =',P3,'kPa')
print('P4 =',P4,'kPa')
# Efficiency Calculation
E = (1-(1/pow(r,(y-1))))*100
print('Efficiency = ',E,'%')
# Plotting Values
pt.xlabel('Volume in (m^3)')
pt.ylabel('Pressure in (kPa)')
pt.plot(V,Pc, label="Compression")
pt.plot([V2,V3],[P2,P3], label="Constant Heat Addition")
pt.plot(V,Pe, label="Expansion")
pt.plot([V1,V4],[P1,P4], label="Constant Heat Addition")
pt.legend()
pt.show()