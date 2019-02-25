import time
startTime = time.time()

import argparse
import numpy as np
from ga import *
from pprint import pprint

# Arguments Parser
def get_arguments():
	ap = argparse.ArgumentParser()
	ap.add_argument('--popSize'    ,type=int,default=100)
	ap.add_argument('--eliteSize'  ,type=int,default=20)
	ap.add_argument('--greedySize' ,type=int,default=5)
	ap.add_argument('--mutateProb' ,type=float,default=0.01)
	
	args = vars(ap.parse_args())
	
	popSize     = args['popSize']
	eliteSize   = args['eliteSize']
	mutateProb  = args['mutateProb']
	
	print '[INFO] Arguments Parsing Done!'
	print '[INFO] Arguments details: '
	print 'popSize,eliteSize       : ',popSize,eliteSize
	print 'mutateProb,generations  : ',mutateProb,generations
	
	return popSize,eliteSize,mutateProb,generations

def get_isEuc(distType):
	if 'non' in distType:
		return 0
	return 1

def readInp():
	isEuc     = get_isEuc(raw_input())
	numPoints = int(raw_input())
	
	pointCoords = [None]*numPoints
	for point in range(numPoints):
		coords  = raw_input()
		coords  = coords.strip()
		pointCoords[point] = [float(c) for c in coords.rsplit(' ')]
	
	pointDist = [None]*numPoints
	for point in range(numPoints):
		dist = raw_input()
		dist = dist.strip()
		pointDist[point] = [float(d) for d in dist.rsplit(' ')]
	
	return numPoints,pointCoords,pointDist

numPoints,pointCoords,pointDist = readInp()
popSize,eliteSize,mutateProb,generations = get_arguments()
geneticAlgo(numPoints,pointDist,popSize,eliteSize,mutateProb,generations,startTime)

# pprint (pointCoords)
# pprint (pointDist)