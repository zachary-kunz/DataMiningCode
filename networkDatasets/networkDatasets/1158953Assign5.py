
## Author: Salem <Salem@SALEM-OFFICE>

import numpy
import random
import time
from matplotlib import pyplot as plt
#import networkx as nx
#filename = "networkDatasets/toyN.txt"
filename = "HprdNetwork.txt"
X = numpy.loadtxt(filename)
n = int(max(max(X[:,0]),max(X[:,1])))
A = numpy.zeros((n,n))
#remember python index the entries from 0 to n-1.
#populate A..iterate over X and populate entries in A
#Then calculate measures..
#print(n, A)

for i in range(len(X[:,0])):
    A[int(X[i,0])-1, int(X[i,1])-1] = 1
    
for j in range(len(X[:,1])):
    A[int(X[j,1])-1, int(X[j,0])-1] = 1
    
#print(A)
#Finding Degrees of each node
degree = numpy.array([0]*n)
for i in range(n):
    for j in range(n):
        if A[i,j] == 1:
            degree[i] += 1
#print(degree)

#Organizing Data into frequencies
sortByFrequency = {}
for i in numpy.sort(degree):
    if i in sortByFrequency:
        sortByFrequency[i] += 1
    else:
        sortByFrequency[i] = 1

#print(sortByFrequency)
#Find the probabilities of each node
probability = []
for i in sortByFrequency:
    probability.append(sortByFrequency[i] / n)
    
#print(probability)

#Plots Data into a graph
fig, (ax1, ax2) = plt.subplots(2)
#Graph one labels
ax1.set_title('Degrees vs. Number on nodes')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
#Graph 2 labels
ax2.set_title('Log by Log Graph')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.loglog(basex = 2, basey = 2)
#Populating graphs with points
for i in range(len(sortByFrequency)):
    j = list(sortByFrequency)[i]
    ax1.scatter(j, sortByFrequency.get(j))
    ax2.scatter(j, probability[i])
plt.tight_layout()

#Cluster Coefficient
clusterC = 0
for i in range(n):
    ids = numpy.where(A[i,:] == 1)[0]
    
    #Accounts for nodes that have a degree less than 2
    if len(ids) <= 2:
        clusterC += 0
    else:
        total = numpy.sum(A[ids,:][:,ids])/2
        maxEdge = len(ids) * (len(ids) - 1) / 2
        clusterC += (total/maxEdge)
        
finalCC = 1/n * clusterC

print("Cluster Coefficient", finalCC)

