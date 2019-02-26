import time
startTime = time.time()

import argparse
import numpy as np
from ga import *

# Arguments Parser
def get_arguments():
	ap = argparse.ArgumentParser()
	ap.add_argument('--popSize'    ,type=int,default=100)
	ap.add_argument('--eliteSize'  ,type=int,default=20)
	ap.add_argument('--greedySize' ,type=int,default=4)
	ap.add_argument('--crossFun'   ,type=str,default='oc')
	ap.add_argument('--mutateProb' ,type=float,default=0.01)
	
	args = vars(ap.parse_args())
	
	popSize     = args['popSize']
	eliteSize   = args['eliteSize']
	greedySize  = args['greedySize']
	crossFun    = args['crossFun']
	mutateProb  = args['mutateProb']
	
	print '[INFO] Arguments Parsing Done!'
	print '[INFO] Arguments details: '
	print 'popSize,eliteSize,greedySize : ',popSize,eliteSize,greedySize
	print 'crossFun,mutateProb          : ',crossFun,mutateProb
	
	return popSize,eliteSize,greedySize,crossFun,mutateProb

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
popSize,eliteSize,greedySize,crossFun,mutateProb = get_arguments()
geneticAlgo(numPoints,pointDist,popSize,eliteSize,greedySize,crossFun,mutateProb,startTime)

# from pprint import pprint
# pprint (pointCoords)
# pprint (pointDist)