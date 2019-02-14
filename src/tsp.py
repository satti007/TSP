import argparse
from ga import *

# Arguments Parser
def get_arguments():
	ap = argparse.ArgumentParser()
	ap.add_argument('--popSize'    ,type=int,default=100)
	ap.add_argument('--eliteSize'  ,type=int,default=10)
	ap.add_argument('--generations',type=int,default=500)
	ap.add_argument('--mutateProb' ,type=float,default=0.01)
	
	args = vars(ap.parse_args())
	
	popSize     = args['popSize']
	eliteSize   = args['eliteSize']
	mutateProb  = args['mutateProb']
	generations = args['generations']
	
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
	
	pointCoords = []
	for point in range(numPoints):
		coords  = raw_input()
		pointCoords.append([float(c) for c in coords.split(' ')])
	
	pointDist = []
	for i in range(numPoints):
		dist = raw_input()
		pointDist.append([float(d) for d in dist.split(' ')])
	
	return numPoints,pointCoords,pointDist

numPoints,pointCoords,pointDist = readInp()
popSize,eliteSize,mutateProb,generations = get_arguments()
geneticAlgo(numPoints,pointDist,popSize,eliteSize,mutateProb,generations)