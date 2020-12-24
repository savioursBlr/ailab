#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Python program to print DFS traversal from a given given graph 
from collections import defaultdict 
  
# This class represents a directed graph using adjacency list representation 
class Graph: 
  
    def __init__(self,vertices): 
        self.V = vertices              # No. of vertices  
        self.graph = defaultdict(list)  # default dictionary to store graph 
  
   
    def addEdge(self,u,v):             # function to add an edge to graph 
        self.graph[u].append(v) 
  
    def printGraph(self):               # function to display the graph 
        print(self.graph)
        
    def DLS(self,src,target,maxDepth):    # A function to perform a Depth-Limited search from given source 'src'
  
        if src == target : return True
  
        if maxDepth <= 0 : return False      # If reached the maximum depth, stop recursing. 
  
        for i in self.graph[src]: 
                if(self.DLS(i,target,maxDepth-1)):      # Recur for all the vertices adjacent to this vertex
                    return True
        return False
    
  
# Create a graph given in the above diagram 
g = Graph (9); 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 4) 
g.addEdge(2, 5) 
g.addEdge(2, 6) 
g.addEdge(3,7)
g.addEdge(3,8)
  
target = 0; maxDepth = 3; src = 0
  
print(g.printGraph())
if g.DLS(src,target,maxDepth) == True:
    print("Target %d is reachable from source %d within max depth %d" %(target,src, maxDepth))
else: 
    print("Target %d is NOT reachable from source %d within max depth %d" % (target,src, maxDepth))


# In[ ]:




