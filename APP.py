import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

# #Small example
# G.add_nodes_from([1,2,3,4,5])
# G.add_edge(1, 3)
# G.add_edge(1, 4)
# G.add_edge(2, 5)
# G.add_edge(3, 2)
# G.add_edge(3, 5)
# G.add_edge(4, 3)
# # Draw graph
# nx.draw(G, with_labels = True)
# plt.show()


# Create Graph
G = nx.Graph()

filepath = "edgelist/BlogCatalog-edgelists.csv"

colNames=["Start", "End"]
edgeData = pd.read_csv(filepath, names=colNames)

edgeData.head()
# edgeData.size
# edgeData.shape
# edgeData[edgeData.isnull().any(axis=1)]

#Add nodes
nodes = []
#loop throug data records
for i in range (0, edgeData.shape[0]):
    #append every node
    nodes.append(edgeData.iloc[i,0])
    nodes.append(edgeData.iloc[i,1])
#creating a set of nodes    
nodes = set(nodes)
#sorting the nodes in increasing order
uniqueNodes = (list(nodes))
uniqueNodes.sort()
#adding the nodes to the graph
G.add_nodes_from(uniqueNodes)

# Add edges
#loop from 0 to amount of records
for i in range (0, edgeData.shape[0]):
    #add the edge to the graph
    G.add_edge(edgeData.iloc[i,0], edgeData.iloc[i,1])
    
    
# Draw graph
# nx.draw(G)
# plt.show()


# Execute 10 times this command sequence
numOperations = 10
for step in range(1, numOperations):
    # Choose a random start node
    vertexid = 1
    # Dictionary that associate nodes with the amount of times it was visited
    visited_vertices = {}
    # Store and print path
    path = [vertexid]
    
    print("Step: %d" % (step))
    # Restart the cycle
    counter = 0
    # Execute the random walk with size 100 (100 steps)
    randomWalkSize = 100
    for counter in range(1, randomWalkSize): 
        # Extract vertex neighbours vertex neighborhood
        vertex_neighbors = [n for n in G.neighbors(vertexid)]
        # Set probability of going to a neighbour is uniform
        probability = []
        probability = probability + [1./len(vertex_neighbors)] * len(vertex_neighbors)
        # Choose a vertex from the vertex neighborhood to start the next random walk
        vertexid = np.random.choice(vertex_neighbors, p=probability)
        # Accumulate the amount of times each vertex is visited
        if vertexid in visited_vertices:
            visited_vertices[vertexid] += 1
        else:
            visited_vertices[vertexid] = 1

        # Append to path
        path.append(vertexid)

    # Organize the vertex list in most visited decresing order
    mostvisited = sorted(visited_vertices, key = visited_vertices.get,reverse = True)
    print("Path: ", path)
    
    # Separate the top 10 most visited vertex
    print("Most visited nodes: ", mostvisited[:10])
    
    








