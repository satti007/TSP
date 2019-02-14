from ga import *

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
geneticAlgo(numPoints,pointDist)