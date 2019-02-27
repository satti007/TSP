#define your helper functions
import random
import numpy as np

np.random.seed(26)
random.seed(26)


def greedyRoute(numPoints,pointDist):
	start = random.randint(0,numPoints)
	curr  = start
	route = [start]
	inRoute = { start : 1 }	
	for i in range(numPoints-1):
		minc = None
		mind = float('inf')
		for j in range(numPoints):
			if j not in inRoute:
				if pointDist[curr][j] < mind:
					minc = j
					mind = pointDist[curr][j]
		
		curr = minc
		inRoute[minc] = 1
		route.append(minc)
	
	return route


def get_alt(m, hashmap):
	while True:
		if m not in hashmap:
			break
		m = hashmap[m]
	return m

def crossOverUtil(parent1, parent2):
	child    = [None]*len(parent1)
	indices  = np.random.randint(low=0,high=len(parent1),size=2)
	startidx = min(indices)
	endidx   = max(indices)
	# child = child + parent1[startidx:endidx+1]
	# child = child + [city for city in parent2 if city not in child]
	child [startidx:endidx+1] = parent1[startidx:endidx+1] 
	
	map_1 = {}
	for i in range(startidx, endidx+1):
		map_1[parent1[i]] = parent2[i]
	
	for i in range(startidx) + range(endidx+1, len(parent1)):
		child[i] = get_alt(parent2[i], map_1)
	
	return child

def mutateUtil(tour,mutateProb):
	if random.random() < mutateProb:
		maxlen = len(tour)
		startidx, endidx = np.random.randint(0, maxlen-1), np.random.randint(0, maxlen-1)
		while endidx == startidx:
			endidx = np.random.randint(0, maxlen-1)	
		startidx, endidx = min(startidx, endidx), max(startidx, endidx)
		
		mid = tour[startidx:endidx+1]
		mid.reverse()
		return tour[:startidx] + mid + tour[endidx+1:]
	
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