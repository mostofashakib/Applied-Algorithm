"""
Reading Link: https://www.geeksforgeeks.org/strongly-connected-components/?ref=rp
Video Link: https://www.youtube.com/watch?v=RpgcYiky7uw
Written by: Mostofa Adib Shakib
Language: Python
Time Complexity: O(V+E)

Algorithm:

1) Create an empty stack ‘S’ and do DFS traversal of a graph. In DFS traversal, after calling recursive DFS for adjacent vertices of a vertex,
push the vertex to stack. In the above graph, if we start DFS from vertex 0, we get vertices in stack as 1, 2, 4, 3, 0.
2) Reverse directions of all arcs to obtain the transpose graph.
3) One by one pop a vertex from S while S is not empty. Let the popped vertex be ‘v’. Take v as source and do DFS (call DFSUtil(v)).
The DFS starting from v prints strongly connected component of v. In the above example, we process vertices in order 0, 3, 4, 2, 1
(One by one popped from stack).
"""

from collections import defaultdict 
   
#This class represents a directed graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    # A function used by DFS 
    def DFSUtil(self,v,visited): 
        # Mark the current node as visited and print it 
        visited[v]= True
        print(v) 
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited) 
  
  
    def fillOrder(self,v,visited, stack): 
        # Mark the current node as visited  
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
        stack = stack.append(v) 
      
  
    # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
        g = Graph(self.V) 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
        return g 
  
   
   
    # The main function that finds and prints all strongly 
    # connected components 
    def printSCCs(self): 
          
         stack = [] 
        # Mark all the vertices as not visited (For first DFS) 
        visited =[False]*(self.V) 
        # Fill vertices in stack according to their finishing 
        # times 
        for i in range(self.V): 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
  
        # Create a reversed graph 
         gr = self.getTranspose() 
           
         # Mark all the vertices as not visited (For second DFS) 
         visited =[False]*(self.V) 
  
         # Now process all vertices in order defined by Stack 
         while stack: 
             i = stack.pop() 
             if visited[i]==False: 
                gr.DFSUtil(i, visited) 
                print("") 
   
# Create a graph given in the above diagram 
g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
   
print ("Following are strongly connected components in given graph")

g.printSCCs() 