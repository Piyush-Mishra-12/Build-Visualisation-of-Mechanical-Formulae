import math
import matplotlib.pyplot as pt
import numpy as ny
l1 = 2 # length of link 1
l2 = 1 # length of link 2
x0 = 0 # Fix postion of link 1 
y0 = 0 # Fix postion of link 1
ct = 1 # A counter variable to save the file name, it is being defined as global variable as ct would be counter after every time function is being called
def robo (ts1,te1,tn1,ts2,te2,tn2): # defining a fuction so that repeatation can be ignored
	t1 = ny.linspace(ts1,te1,tn1) # Defining an array for theta 1
	t2 = ny.linspace(ts2,te2,tn2) # Defining an array for theta 2
	for T1 in t1: # for every value of theta 1 in loop 
		for T2 in t2: # for every value of theta 2 in loop with loop of theta 1	
			x1 = l1*math.cos(T1) # calculation for link 1
			y1 = l1*math.sin(T1)
			if ts1 != 0 and te1 == 0 and tn1 != 1: # soecifying positing of link 2 and at different postion of link 1
				x2 = x1 + l2*math.cos(T2) # Calculation for link 2
				y2 = y1 + l2*math.sin(T2)
			elif ts1 != 0 and te1 == 0 and tn1 != 1:
				x2 = x1 - l2*math.cos(T1 + math.pi/2)
				y2 = y1 - l2*math.sin(T1 + math.pi/2)
			elif ts1 == 0 and te1 != 0 and tn1 == 1:
				x2 = x1 - l2*math.cos(T2)
				y2 = y1 - l2*math.sin(T2)	
			else:
				x2 = x1 + l2*math.cos(T1 + math.pi/2)
				y2 = y1 + l2*math.sin(T1 + math.pi/2)
			global ct # Calling the global counter variable so that filename can be saved and change according to our wish
			filename = 'arm' + str(ct) + '.png' # Defining a string variable for saving name for graph
			ct = ct +1 # Appending value for ct so that overwriting is avoided
			pt.figure() # Saving the graph in an array
			pt.plot([x0,x1],[y0,y1])# Ploting graph
			pt.plot([x1,x2],[y1,y2])
			pt.xlim([-3,3]) # Specifying limits of the graph
			pt.ylim([-3,3])
			pt.savefig(filename) # Saving the graph with different graph
robo(math.pi,0,75, math.pi*3/2,math.pi/2,75) # Calling fuctions while specifing various positons for link 1 and link 2
robo(math.pi,0,75, math.pi/2,math.pi,1)
robo(0,math.pi,1, math.pi/2,math.pi*3/2,75)
robo(0,math.pi,75, math.pi,math.pi*3/2,1)