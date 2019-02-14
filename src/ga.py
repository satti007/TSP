from utils import *
from sys import stdout
import numpy as np

def mutation(childPopulation, mutateProb):
#returns children after mutation of dim popSize x numPoints

def crossOver(selPopulation):
#returns children after cross-over of dim popSize x numPoints

def selection(population,numPoints,pointDist,popSize,eliteSize):
#returns a selected population of dim popSize x numPoints

def initPopulation(numPoints, popSize):
#returns a random population of dim popSize x numPoints

def geneticAlgo(numPoints,pointDist,popSize,eliteSize,mutateProb,generations):

	pop = initPopulation(numPoints, popSize)
	while True:
		for gen in range(0,generations):
			pop = selection(pop,numPoints,pointDist,popSize,eliteSize)
			pop = crossOver(pop)
			pop = mutation(pop, mutateProb)
			stdout.flush()
			if gen == 10:
				break
		break



