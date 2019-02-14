from sys import stdout

def geneticAlgo(numPoints,pointDist,popSize,eliteSize,mutateProb,generations):
	while True:
		for gen in range(0,generations):
			print gen
			stdout.flush()
			if gen == 10:
				break
		break