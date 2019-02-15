#define your helper functions
import random
import numpy as np

def crossOverUtil(parent1, parent2):
	child    = []
	indices  = np.random.randint(low=0,high=len(parent1),size=2)
	startidx = min(indices)
	endidx   = max(indices)
	
	child = child + parent1[startidx:endidx+1]
	child = child + [city for city in parent2 if city not in child]
	
	return child

def mutateUtil(tour,mutateProb):
	# for i in range(len(tour)):
	# 	if random.random() < mutateProb:
	# 		ind = np.random.randint(low=0,high=len(tour))
	# 		temp = tour[i]
	# 		tour[i] = tour[ind]
	# 		tour[ind] = temp
	
	if random.random() < mutateProb:
		maxlen = len(tour)
		split_1, split_2 = np.random.randint(0, maxlen-1), np.random.randint(0, maxlen-1)
		while split_2 == split_1:
			split_2 = np.random.randint(0, maxlen-1)	
		split_1, split_2 = min(split_1, split_2), max(split_1, split_2)

		mid = tour[split_1:split_2+1]
		mid.reverse()
		return tour[:split_1] + mid + tour[split_2+1:]

	return tour

def randomRoute(numPoints):
	return random.sample(range(0,numPoints),numPoints)

def routeCost(route, pointDist, flag=None):
	cost = 0.0
	for i in range(0,len(route)-1):
		cost = cost + pointDist[route[i]][route[i+1]]
	
	return cost

def getFitness(population, pointDist):
	routeTofit = {}
	for idx,route in enumerate(population):
		routeTofit[idx] = (1.0/routeCost(route, pointDist))
	
	return routeTofit

def selectProbability(routeTofit):
	total   = sum(routeTofit.itervalues())
	selProb = [float(f)/total for r,f in routeTofit.iteritems()]
	
	return selProb

def bestRoute(population,pointDist):
	minCost     = float('inf')
	bestRouteId = -1
	for idx,route in enumerate(population):
		currCost = routeCost(route,pointDist)
		if minCost > currCost: 
			minCost     = currCost
			bestRouteId =  idx
	
	return minCost, bestRouteId

def printRoute(route):
	for city in route:
		print city,
	print ''