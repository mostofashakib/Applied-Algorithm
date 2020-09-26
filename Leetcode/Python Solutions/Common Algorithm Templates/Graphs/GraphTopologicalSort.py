"""
Graph Topological sort > Modified DFS Traversal
Time complexity: O(V+E)  * V = Vertices & E = Edge

Algorithm:

1) Pick an unvisited node and mark it as visited
2) Recursively call the helper method to visit all of it's unvisited neightbours
3) When all the neighbours of a given node is visited put the value on a stack starting from the last recursive call
4) Pick another unvisited node and repeat step 1-3 upuntil all the nodes are visited 

First recursively call topological sorting for all its adjacent vertices, then push it to a stack. Finally, print contents of stack.
Note that a vertex is pushed to stack only when all of its adjacent vertices (and their adjacent vertices and so on) are already in stack.

"""

from collections import defaultdict   # in defaul dictionary all the keys are numbered automatically

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list) # creates a default dictonary of adjacency matrix

    def addEdge(self, u,v):
        self.graph[u].append(v)
    
    def topologicalSortHelper(self, v, visited, stack):
        visited[v] = True # marks a node as visited

        for i in self.graph[v]: # visites all the neighbours of a node
            if visited[i] == False:  # recursively calls the function if it's neighbours are unvisited
                self.topologicalSortHelper(i, visited, stack)
        
        stack.append(v)  # inserts the node starting from the last recursive call

    def topologicalSort(self):
        visited = [False] * self.V  # creates an array of unvisited nodes
        stack = []   # creates a stack to store the values

        for i in range(self.V):   # visites all the nodes
            if visited[i] == False:    #if a node is unvisited then recursively calls all of it's neighbours
                self.topologicalSortHelper(i, visited, stack)
        
        print(stack[::-1])  # prints the result starting from the value at the top of the stack


g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print ("Following is a Topological Sort of the given graph")
g.topologicalSort() 