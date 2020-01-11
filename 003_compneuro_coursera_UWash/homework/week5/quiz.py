import numpy as np
import pickle
import matplotlib.pyplot as plt


def membrane(plotflag=True):
	# from __future__ import print_function
	"""
	Created on Wed Apr 22 15:53:00 2015

	Charging and discharging curves for passive membrane patch
	R Rao 2007

	translated to Python by rkp 2015
	"""

	# import numpy as np
	# import matplotlib.pyplot as plt

	# input current
	I = 10 # nA

	# capacitance and leak resistance

	C = 0.1 # nF
	R = 100 # M ohms
	tau = R*C # = 0.1*100 nF-Mohms = 100*100 pF Mohms = 10 ms
	print('C = %.3f nF' % C)
	print('R = %.3f M ohms' % R)
	print('tau = %.3f ms' % tau)
	print('(Theoretical)')

	# membrane potential equation dV/dt = - V/RC + I/C

	tstop = 150 # ms

	V_inf = I*R # peak V (in mV)
	tau = 0 # experimental (ms)

	h = 0.2 # ms (step size)

	V = 0 # mV
	V_trace = [V] # mV

	for t in np.arange(h, tstop, h):

	   # Euler method: V(t+h) = V(t) + h*dV/dt
	   V = V +h*(- (V/(R*C)) + (I/C))

	   # Verify membrane time constant
	   if (not tau and (V > 0.6321*V_inf)):
	     tau = t
	     print('tau = %.3f ms' % tau)
	     print('(Experimental)')

	   
	   # Stop current injection 
	   if t >= 0.6*tstop:
	     I = 0

	   V_trace += [V]
	   if t % 10 == 0:
	       plt.plot(np.arange(0,t+h, h), V_trace, color='r')
	       plt.xlim(0, tstop)
	       plt.ylim(0, V_inf)
	       plt.draw()
	       
	if plotflag:
		plt.show()

	return

def Q(nums):

	for num in nums:

		if num==1:
			# When plotting "spikes" what is on the y-axis?

			print('Q1: Voltage spikes are plotted (although current seemingly would suffice as well)')
			
		if num==2:
			# RC circuit, what corresponds to r,c,source?

			print('Q2: Battery = Ion concentration gradient, resistor = ion channel, capacitor = lipid bilayer')

		if num==3:
			# If a neuron with -100mV equilibrium potential (-65mV resting cell potential) opens ion channels, what happens?

			print('Q3: Hyperpolarize the cell, thus decreasing the membrane potential')
			#Thought we were talking absolute value of the membrane potential, vocab differences will take some time...

		if num==4:
			# Suppose 5 subunits and ball-in-socket. What is expression for current across membrane?

			print('Q4: Needs a u^5 and a z^1')

		if num==5:
			#Assume Na with fast "m" dynamics and slower "h" dynamics, as described in picture. With current injection that takes membrane V from -65mV to -75mV, what reaches steady state first?

			print('Q5: m, h has farther to go and slower dynamics')
			
		if num==6:
			#How can cells depolarize to >-30mV during Na+ spike?

			print('Q6: h is too slow to block')

		if num==7:
			# All neural coding can be reduced to variations in firing rate

			print('Q7: False!')
			#Originally thought it was true just for this class, but we are already looking big picture!

		if num==8:
			# Recall exponential integrate and fire model. How many stable fixed points in system?

			print('Q8: 1, just the stable zero crossing')
			#Originally had 2, missed the stable requirement

		if num==9:
			#FitzHugh-Nagumo model, what is expression for w-nullcline?

			print('Q9: bV = cw, it is where dw/dt goes to 0')

		if num==10:
			#Where on the chart is the upstroke?

			print('Q10: Region D, where V starts to increase')

		if num in [11,12,13,14,15]:

			#Provided function:
			# membrane(plotflag=False)

			#Given, what is steady state voltage?
			I = 10E-9
			R = 100E6
			C = 0.10E-9

			V_inf = R*I
			print('Q11: ' + str(round(V_inf*1E3,0)) + 'mV')
			#Originally had 10 due to typo

			#Does it reach stable value faster/slower after increasing R?
			print('Q12: Slower, Time constant increases')

			#What about after reducing C?
			print('Q13: Faster, tau decreases')
			
			#What about increasing R and decreasing C by same amount?
			print('Q14: No change, tau is same')

			#Why is tau 63%? In derivation what is solution to DE?
			print('Q15: Classic solution, (1-e^(-t/tau))')

		if num in [16,17,18]:
			#What current makes it stop firing?
			#could do this in a loop and show it, but just trust me here
			print('Q16: 250pA')

			#Fastest rate? 
			#Probably only bounded by refractory period, which is 5(ms?)
			t_ref = 0.005
			print('Q17: 167')
			#Originally had 1/refractory. Seems like a better answer to me as this is limited by propagation method?

			#Mess with noise script, what happens?
			print('Q18: Distribution gets exponential looking')

	return


Q([1,2,3,4,5,6,7,8,9,10,11,16])
# Q([11])