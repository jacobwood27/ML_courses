import numpy as np
import pickle
import matplotlib.pyplot as plt

def Q(nums):

	for num in nums:

		if num==1:
			# What feed-forward network will fuzz up the image?

			print('Q1: We want to spread things out around the diagonal, so the one with all the 3s')
			
		if num==2:
			# What network globally darkens the image?

			print('Q2: We do not want to change the structure, just all the values. Numbers only on the diagonals. The 0.5s')

		if num==3:
			# What network picks out some edges?

			print('Q3: The 0.75s. Finds strong gradients.')

		if num==4:
			# What network makes an ugly image?

			print('Q4: The useless one with the 1s')

		if num==5:
			# Which of these many assumptions are we making?

			print('Q5: All the stuff about no dynamics')

		if num==6:
			# How do things vary with alpha_neuron.py's t_peak?

			print('Q6: Increasing sublinearly. Weird word.')

		if num==7:
			# What is the explanation for 6?

			print('Q7: Decrease in the conductive decay rate')

		if num==8:
			# What is E_syn for an inhibitory synapse?

			print('Q8: Less than equilibrium potential and threshold potential')

		if num==9:
			#Given these matrices:
			W = np.zeros((5,5)) + 0.1
			np.fill_diagonal(W,0.6)
			
			u = np.array([0.6,0.5,0.6,0.2,0.1])

			M = np.array([[-0.25,0,.25,.25,0],[0,-.25,0,.25,.25],[.25,0,-.25,0,.25],[.25,.25,0,-.25,0],[0,.25,.25,0,-.25]])

			h = np.matmul(W,u)

			M_eigs = np.linalg.eigh(M)
			M_eigvals = M_eigs[0]
			M_eigvecs = M_eigs[1]

			v_ss = np.zeros(5)
			for val,vec in zip(M_eigvals,M_eigvecs.transpose()):
				v_ss += (np.dot(h,vec) / (1-val)) * vec

			print('Q9: V_ss = ' + str(v_ss))


	return


Q([1,2,3,4,5,6,7,8,9])
