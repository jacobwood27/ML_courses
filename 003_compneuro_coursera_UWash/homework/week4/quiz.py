import numpy as np
import pickle
import matplotlib.pyplot as plt

def discrete_entropy(p_i):
	return -sum(p_i * np.log2(p_i))


def Q(nums):

	for num in nums:

		if num==1:
			# Bernoulli Distribution
			# P(F=1) = 0.1
			# What is entropy H(F)?
			#
			# Discrete distribution entropy: H(X) = -sum(p(x)log(p(x)))
			# Possible states are 0 and 1 
			p_i = np.array([0.1,0.9])
			H = discrete_entropy(p_i)

			print('Q1: ' + str(round(H,3)))
			
		if num==2:
			#P(S) = 0.1
			#P(F|S) = 1/2
			#P(F|!S) = 1/18
			#Mutual Information: I(X;Y) = H(X) - H(X|Y)
			#					 I(X;Y) = H(Y) - H(Y|X)
			#					 I(X;Y) = H(X) + H(Y) - H(X,Y)
			#					 I(X;Y) = H(X,Y) - H(X|Y) - H(Y|X)
			#Conditional Entropy: H(Y|X) = -sum(p(x,y)log(p(x,y)/p(x)))
			P_S = 0.1
			P_FgS = 1./2.
			P_FgnS = 1./18.

			H_Fgs = np.array([discrete_entropy(np.array([P_FgS,(1-P_FgS)])),discrete_entropy(np.array([P_FgnS,(1-P_FgnS)]))])
			P_s = np.array([P_S,1-P_S])
			avg_noise_entropy = sum(P_s*H_Fgs)
			P_F = sum(P_s * np.array([P_FgS,P_FgnS]))
			H_F = discrete_entropy(np.array([P_F,1-P_F]))
			I = H_F - avg_noise_entropy

			print('Q2: ' + str(round(I,4)))

		if num==3:
			print('Q3: The pieces that make things up')

		if num==4:
			print('Q4: The error')

		if num==5:
			print('Q5: The weights, or transparency in this example')
			
		if num==6:
			print('Q6: The extra costs')

		if num in [7,8,9,]:
			with open('tuning_34.pickle','rb') as f:
				data = pickle.load(f)

			plt.figure()
			for n in ['neuron1','neuron2','neuron3','neuron4']:
				s = data['stim']
				r = data[n]
				mr = np.mean(np.array(r),axis=0)
				plt.plot(s,mr,label=n)
			plt.legend()
			plt.xlabel('Stimulus Direction [degrees]')
			plt.ylabel('Mean Firing Rate [Hz]')
			# plt.draw()
			# plt.pause(0.001)

			print('Q7: Looks like a half wave rectified cosine to me!')

			#In Poisson distributions the Fano factor, or variance/mean, is just about 1. 
			for n in ['neuron1','neuron2','neuron3','neuron4']:
				r = data[n]
				d = np.mean(np.array(r),axis=0)

				meanval = np.mean(d)
				variance = 1/(s[1] - s[0])*np.var(d)
				F = meanval/variance
				# print(n + ': Fano = ' + str(round(F,3)))

			print('Q8: Neuron 3')

			with open('pop_coding_34.pickle','rb') as f:
				popc = pickle.load(f)

			mfr_1_norm = np.mean(popc['r1']) / np.max(np.mean(np.array(data['neuron1']),axis=0))
			mfr_2_norm = np.mean(popc['r2']) / np.max(np.mean(np.array(data['neuron2']),axis=0))
			mfr_3_norm = np.mean(popc['r3']) / np.max(np.mean(np.array(data['neuron3']),axis=0))
			mfr_4_norm = np.mean(popc['r4']) / np.max(np.mean(np.array(data['neuron4']),axis=0))
			
			nb = popc['c1'] * mfr_1_norm + popc['c2'] * mfr_2_norm + popc['c3'] * mfr_3_norm + popc['c4'] * mfr_4_norm


			a = 90 - np.arctan2(nb[1],nb[0]) * 180./np.pi

			print('Q9: ' + str(round(a)))






			
	return


Q([1,2,3,4,5,6,7])