from utils import *
from sys import stdout
import numpy as np

def mutation(childPopulation, mutateProb, popSize):
#returns children after mutation of dim popSize x numPoints
	for i in range(popSize):
		if np.random.random() < mutateProb:
			childPopulation[i] = mutationUtil(childPopulation[i], mutateProb)

	return childPopulation

def crossOver(selPopulation, popSize):
#returns children after cross-over of dim popSize x numPoints
	selPopulation1, selPopulation2 = selPopulation[:popSize/2], selPopulation[popSize/2:]
	childPopulation = [None]*popSize
	for x in xrange(popSize/2):
		childPopulation[x], childPopulation[x+(popSize/2)] = crossOverUtil(selPopulation1[x],selPopulation2[x])
	
	return childPopulation

def selection(population,numPoints,pointDist,popSize,eliteSize):
#returns a selected population of dim popSize x numPoints

def initPopulation(numPoints, popSize):
#returns a random population of dim popSize x numPoints

def geneticAlgo(numPoints,pointDist,popSize,eliteSize,mutateProb,generations):

	pop = initPopulation(numPoints, popSize)
	while True:
		for gen in range(0,generations):
			pop = selection(pop,numPoints,pointDist,popSize,eliteSize)
			pop = crossOver(pop, popSize)
			pop = mutation(pop, mutateProb, popSize)
			stdout.flush()
			if gen == 10:
				break
		break



