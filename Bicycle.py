#FLow Over Bicycle

#Inmporting the possibly required Library
import matplotlib.pyplot as pt # math libaray is not imported becuse its use was not there
import numpy as ny # we imported so that area of different postion can be treated as different value in the array giving us plot at same graph
import random # Here we imported random libaray so that every time we run the program it will plot the graph for any random value of velocity and coefficient of drag

#Taking input
Cd = random.randrange(0, 999) #Cd is Range of Coefficient of drag
V = random.randrange(0,295) #V is Range of Velocity of bicycle (m/s) ->  {295m/s is the highest speed recorded for bicycle}
rho = 1.1849 # Density of the fluid hitting the area in (kg/m^3) -> {As our climate is little hotter although Pressure is 1 atm only}
Force1 = [] #Drag Force Calculated in (kgm/s^2)
Force2 = [] #Drag Force Calculated in (kgm/s^2)
A = ny.array([0.533, 0.423, 0.381, 0.343, 0.244], dtype= float) # Frontal Area will be varied as we'll change it due to changing postion of cyclist

for cd in range(0,999): # Coefficient of drag values are put in for loop 
#So that even if constant frontal area of various positon are changed but due to other aspects such helmet or types of wearable gears Cd does affect
	F = 0.5*cd*A*rho*V*V/1000 # We defined F because if we normally append its value then the printable output will be diffcult to understand
	# we have divided by 1000 becuz random float values were not able to execute of
	Force1.append(F) # If we weren't append its value then we would not have got our plot
	print(cd,'-',F, 'Velocity =',V) # here We getting the Output of Cd wrt Force as well as it will also mention the random value of Velocity that has been taken
pt.plot(Force1) # Ploting the Force
pt.legend(["Upright", "Backup", "Elbow", "Pantani", "Superman"])
pt.xlabel(' Coefficient of drag (x/1000)')
pt.ylabel('Drag Force (in N)')
pt.title("Drag Force vs Coefficient of drag Velocity")
pt.savefig('Cd')
pt.show()

for v in range(0,295): # Velocity of bicycle (m/s) values are put in for loop 
	F = 0.5*Cd*A*rho*v*v/1000
	Force2.append(F)
	print(v,'-',F, 'Coefficient of drag =',Cd)
pt.plot(Force2)
pt.legend(["Upright", "Backup", "Elbow", "Pantani", "Superman"])
pt.xlabel('Velocity (in m/s)')
pt.ylabel('Drag Force (in N)')
pt.title("Drag Force vs Velocity")
pt.savefig('V')
pt.show()