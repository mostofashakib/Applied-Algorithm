"""

This is an exaple of Graph traversal using Depth First Search approach and Adjacency list.

A default dictionary is very similar to a usual dictionary the only difference is that a default dictionary will have default value if 
key is not assigned.

"""


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        print(self.graph)

    def dfshelper(self, v, visited):
        visited[v] = True

        print(v, end = ' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfshelper(i, visited)

    def dfs(self, v):
        visited = [False] * len(self.graph)

        return self.dfshelper(v, visited)

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)


print("Following is DFS from (starting from vertex 0)") 
g.dfs(2) 