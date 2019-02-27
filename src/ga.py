import time
import operator
import numpy as np
from utils import *
from sys import stdout
from pprint import pprint
import matplotlib.pyplot as plt

np.random.seed(26)
random.seed(26)

# returns children after mutation of dim (popSize x numPoints)
def mutation(childPopulation, mutateProb, popSize):
	mutPopulation = [None]*popSize
	
	for i in range(popSize):
		mutPopulation[i] = mutateUtil(childPopulation[i], mutateProb)
	
	return mutPopulation

# returns children after cross-over of dim (popSize x numPoints)
def crossOver(selPopulation, popSize, numPoints, eliteSize):
	childPopulation = [None]*popSize
	
	for i in range(eliteSize):
		childPopulation[i] = selPopulation[i]
	
	random.shuffle(selPopulation)
	for i in range(popSize - eliteSize):
		childPopulation[eliteSize + i] = crossOverUtil(selPopulation[i],selPopulation[popSize-i-1])
	
	return childPopulation

# returns a selected population of dim (popSize x numPoints)
def selection(population, numPoints, pointDist, popSize, eliteSize):
	selPopulation = [None]*popSize
	routeTofit = getFitness(population, pointDist)
	selProb    = selectProbability(routeTofit)
	routeTofit = sorted(routeTofit.items(),key = operator.itemgetter(1),reverse = True)
	
	for i in range(eliteSize):
		selPopulation[i] = population[routeTofit[i][0]]

	for i in range(popSize - eliteSize):
		idx = np.random.choice(range(popSize), p = selProb)
		selPopulation[eliteSize+i] = population[idx]
	
	return selPopulation

# returns a random population of dim ([popSize] x numPoints)
def initPopulation(numPoints,pointDist,popSize,greedySize):
	randomPop = [None]*(popSize - greedySize)
	greedyPop = [None]*greedySize
	for i in range(0,popSize - greedySize):
		randomPop[i] = randomRoute(numPoints)
	
	for i in range(0,greedySize):
		greedyPop[i] = greedyRoute(numPoints,pointDist)
	
	return randomPop + greedyPop

def elitePop(selPop,pop,numPoints,pointDist,eliteSize):
	routeTofit1 = getFitness(selPop,pointDist)
	routeTofit2 = getFitness(pop,pointDist)
	routeTofit2 = sorted(routeTofit2.items(),key = operator.itemgetter(1),reverse = True)
	routeTofit1 = sorted(routeTofit1.items(),key = operator.itemgetter(1),reverse = True)
	population = []
	for i in range(eliteSize):
		population.append(pop[routeTofit2[i][0]])
	
	for i in range(eliteSize):
		population.append(selPop[routeTofit1[i][0]])
	
	return population



# Genetic Algorithm
def geneticAlgo(numPoints,pointDist,popSize,eliteSize,mutateProb,generations,startTime):
	tourCost = float('inf')
	genCosts = []
	pop = initPopulation(numPoints,pointDist,popSize,3)
	minCost, bestRouteId = bestRoute(pop,pointDist)
	print '0', minCost
	genCosts.append(minCost)
	# printRoute(pop[bestRouteId])
	
	while time.time() - startTime < 300:
	# while True:
		for gen in range(0,generations):
			pop = selection(pop, numPoints, pointDist, popSize, eliteSize)
			selPop = pop
			pop = crossOver(pop, popSize, numPoints, eliteSize)
			pop = mutation(pop,  mutateProb, popSize)
			pop = elitePop(selPop,pop,numPoints,pointDist,eliteSize)
			minCost, bestRouteId = bestRoute(pop,pointDist)
			if tourCost > minCost:
				print gen+1, minCost
				tourCost = minCost
				# printRoute(pop[bestRouteId])
			genCosts.append(minCost)
			stdout.flush()
	
	plt.plot(genCosts)
	plt.ylabel('cost')
	plt.xlabel('generation')
	plt.show()