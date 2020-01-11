import numpy as np
import pickle
import matplotlib.pyplot as plt

def Q(nums):

	for num in nums:

		if num==1:
			# Steady state weights if given correlation matrix for Hebbian learning?
			Q = np.array([[0.2,0.1],[0.1,0.15]])

			#We expect the weights to approach the principal eigenvector
			Q_eig = np.linalg.eigh(Q)
			princ = np.argmax(Q_eig[0])

			print('Q1: Some multiple of ' + str(Q_eig[1][princ]))
			
		if num==2:
			# What does weight vector from Q1 tell us?

			print('Q2: None of these things')

		if num==3:
			# Check the things that are true about learning rates

			print('Q3: More noise susceptible, constant remains sensitive (as opposed to 1/time)')

		if num==4:
			# Why do we need to use two steps to update parameters?

			print('Q4: Mutually dependent, local max')

		if num in [5,6,7,8,9]:
			# How do we turn to discrete?

			print('Q5: Make the differential elements deltas')

			# How do we turn discrete into update?

			print('Q6: Algebra')

			# What is the explanation for 6?
			with open('c10p1.pickle', 'rb') as f:
				data = pickle.load(f)
				x = data['c10p1'][:,0]
				y = data['c10p1'][:,1]
			eta = 1
			alpha = 1
			dt = 0.01
			n_iter = 100000

			# Correct for the mean shift
			x = x - np.mean(x)
			y = y - np.mean(y)

			# #Plot
			# plt.scatter(x,y)
			# plt.show()

			for _ in range(5):
				w = np.random.random([2])

				n = 0
				for ii in range(n_iter):
					if n == len(x):
						n = 0
					u = np.array([x[n],y[n]])
					v = np.dot(u,w)
					w = w + dt * eta * (v * u - alpha * v**2 * w)
				print(w)

			print('Q7: Two vectors parallel to the principal eigenvector')

			# What if data is not mean centered?
			for _ in range(5):
				w = np.random.random([2])

				n = 0
				for ii in range(n_iter):
					if n == len(x):
						n = 0
					u = np.array([x[n] + 10,y[n] + 2.2])
					v = np.dot(u,w)
					w = w + dt * eta * (v * u - alpha * v**2 * w)
				print(w)

			print('Q8: Converges to vectors that point at the mean')

			# What if we used pure Hebb?:

			print('Q9: No convergence')


	return


Q([1,2,3,4,5])
