import numpy as np

#define your helper functions

def crossOverUtil(selTour1, selTour2):
	#returns children of dim numPoints
	indices = np.random.randint(high=len(selTour1), size=2)
	low, high = min(indices), max(indices)
	gene1 = selTour1[low:high+1]
	child1 = [None]*len(selTour1)
	child1[low:high+1] = gene1
	for i,x in enumerate(selTour2):
		if i<low or i>high:
			if x not in gene1:
				child1[i] = x
		else:
			continue

	indices = np.random.randint(high=len(selTour1), size=2)
	low, high = min(indices), max(indices)
	gene2 = selTour2[low:high+1]
	child2 = [None]*len(selTour2)
	child2[low:high+1] = gene2

	for i,x in enumerate(selTour1):
		if i<low or i>high:
			if x not in gene2:
				child2[i] = x
		else:
			continue

	return child1, child2

def mutateUtil(tour,mutateProb):
	for i in range(len(tour)):
		if np.random.random() < mutateProb/2:
			ind = np.random.randint(high=len(tour))
			temp = tour[i]
			tour[i] = tour[ind]
			tour[ind] = temp

	return tour


