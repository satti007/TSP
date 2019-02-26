import os
import time
import operator
import numpy as np
from utils import *
from sys import stdout
from pprint import pprint
import matplotlib.pyplot as plt

# returns children after mutation of dim (popSize x numPoints)
def mutation(childPopulation,mutateProb,popSize):
	mutPopulation = [None]*popSize
	
	for i in range(popSize):
		mutPopulation[i] = mutateUtil(childPopulation[i], mutateProb)
	
	return mutPopulation

# returns children after cross-over of dim (popSize x numPoints)
def crossOver(selPopulation,popSize,numPoints,eliteSize):
	childPopulation = [None]*popSize
	
	for i in range(eliteSize):
		childPopulation[i] = selPopulation[i]
	
	random.shuffle(selPopulation)
	for i in range(popSize - eliteSize):
		childPopulation[eliteSize + i] = crossOverUtil(selPopulation[i],selPopulation[popSize-i-1])
	
	return childPopulation

# returns a selected population of dim (popSize x numPoints)
def selection(population,numPoints,pointDist,popSize,eliteSize):
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

# Genetic Algorithm
def geneticAlgo(numPoints,pointDist,popSize,eliteSize,greedySize,crossFun,mutateProb,startTime):
	genCosts = []
	pop = initPopulation(numPoints,pointDist,popSize,greedySize)
	minCost, bestRouteId = bestRoute(pop,pointDist)
	print '0', minCost
	genCosts.append(minCost)
	# printRoute(pop[bestRouteId])
	
	gen = 0
	while time.time() - startTime < 10:
	# while True:
	# for gen in range(1000):
		pop = selection(pop, numPoints, pointDist, popSize, eliteSize)
		pop = crossOver(pop, popSize, numPoints, eliteSize)
		pop = mutation(pop,  mutateProb, popSize)
		minCost, bestRouteId = bestRoute(pop,pointDist)
		print gen+1, minCost
		genCosts.append(minCost)
		# printRoute(pop[bestRouteId])
		stdout.flush()
		gen += 1 
	
	os.system('rm *.pyc')
	plt.plot(genCosts)
	plt.ylabel('cost')
	plt.xlabel('generation')
	plt.show()