import random
import numpy as np

numPoints = 50

print 'euclidean'
print numPoints

coords = []
for i in range(numPoints):
	x = random.uniform(-1, 1)*100
	y = random.uniform(-1, 1)*100
	print str(x)+' '+str(y)
	coords.append([x,y])

# print coords

for i in range(numPoints):
	for j in range(numPoints):
		print str(np.sqrt((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2 )),
	print ''
