"""

This is an example of how to detect cycle in a directed acyclic graph (DAG)

"""

# Solution 1: Breath-First-Search

from collections import defaultdict 
  
def detectCycleInaDirectedGraph(self):
    vertices = [0, 1, 2, 3]             # This can change
    graph = defaultdict(list)
    noOfEdges = len(vertices)
    in_degree = {}

    # Build the graph
    graph[0].append(1)
    graph[0].append(2)
    graph[1].append(2)
    graph[2].append(0)
    graph[2].append(3)
    graph[3].append(3)

    # Buidling the n-degree array

    for i in vertices:
        in_degree[i] = 0

    for i in vertices:
        for j in graph[i]:
            in_degree[j] += 1

    queue = []

    for i in vertices:
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    count = 0

    while queue:
        u = queue.pop(0)
        result.append(u)

        for i in graph[u]:
            in_degree[i] -= 1

            if in_degree[i] == 0:
                queue.append(i)
              
    count += 1

    # If this condition is true then there is a cycle

    if count != noOfEdges:
        return ""
      
    else:
        return ''.join(result)


# Solution 2: Depth-First-Search


from collections import defaultdict 
  
class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def isCyclicUtil(self, v, visited, recStack): 
  
        # Mark current node as visited and  
        # adds to recursion stack 
        visited[v] = True
        recStack[v] = True
  
        # Recur for all neighbours 
        # if any neighbour is visited and in  
        # recStack then graph is cyclic 
        for neighbour in self.graph[v]: 
            if visited[neighbour] == False: 
                if self.isCyclicUtil(neighbour, visited, recStack) == True: 
                    return True
            elif recStack[neighbour] == True: 
                return True
  
        # The node needs to be poped from  
        # recursion stack before function ends 
        recStack[v] = False
        return False
  
    # Returns true if graph is cyclic else false 
    def isCyclic(self): 
        visited = [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V): 
            if visited[node] == False: 
                if self.isCyclicUtil(node,visited,recStack) == True: 
                    return True
        return False
  
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

if g.isCyclic() == 1: 
    print "Graph has a cycle"
else: 
    print "Graph has no cycle"