"""
LeetCode Problem 207. Course Schedule

Link: https://leetcode.com/problems/course-schedule/
Written by: Mostofa Adib Shakib
Language: Python

"""


"""

Course Schedule: Detecting Cycle in a directed Graph

Firstly, we need to finish prerequisites courses before taking a main course so this is a directed graph problem.
In other words, this problem can be restated to Detect cycle in a directed graph or similarly Check if a graph is acyclic.

Secondly, while edges list together with adjacency list and adjacency matrix are three main ways to represent a graph, it's not commonly used to solve graph problems.
One main reason is that to perform a common operation like getting all descendants of a given vertex it takes O(len(edgesList))
Hence, we can first build an adjacency list from the edges list which takes O(1) to perform such operation.

A graph has a cycle if there is a backedge

Back  Edge:

1) There is an edge if there is an edge from to node to itself(self loop)
2) There is an edge from an ancestor to it's parent.

Algorithm to detect a back edge:

1) Keep track of vertices currently in the recursion stack for DFS traversal.
2) If a vertex is both visited and is on the recursion stack then there is a cycle

Complexity Analysis
Time Complexity: O(V + E) where V is the number of vertices and E is the number edges.

Space Complexity: O(V + E) the adjacency list dominates our memory usage.

"""


"""
Solution 1 - Topological Sort with DFS
"""

from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.graph = defaultdict(list)                       # initializes a dictionary
    
    def helper(self, u, visited, recStack):
        visited[u] = True                # marks a node as visited
        recStack[u] = True               # marks the current node as visited 
        
        for i in self.graph[u]:
            if visited[i] == False:
                if self.helper(i, visited, recStack) == True:   #check if there is an edge from a parent to it's ancestor
                    return True
            elif recStack[i] == True:   #checking for self loops
                return True
        
        recStack[u] = False
        return False
    
    def isCycle(self, n):              
        visited = [False] * n      # visited array
        recStack = [False] * n     # recursive calls
        
        for i in range(n):         # traverse all the nodes
            if visited[i] == False:
                if self.helper(i, visited, recStack) == True:  # recursively visit all the node's neighbour
                    return True
        return False
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        for i,j in prerequisites:
            self.graph[i].append(j)   #make a adjacencyList
            
        if self.isCycle(numCourses) == True:
            return False
        else:
            return True

def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        # c2 (course 2) is a prerequisite of c1 (course 1)
        # i.e c2c1 is a directed edge in the graph
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList


"""
Solution 2: DFS with an array storing 3 different states of a vertex

It's also similar to this article Python DFS + Memoization where we use an array for Memoization.
"""

class Solution:
    def buildAdjacencyList(self, n, edgesList):
        ...
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build Adjacency list from Edges list
        adjList = self.buildAdjacencyList(numCourses, prerequisites)

        # Each vertex can have 3 different states:
        # state 0   : vertex is not visited. It's a default state.
        # state -1  : vertex is being processed. Either all of its descendants
        #             are not processed or it's still in the function call stack.
        # state 1   : vertex and all its descendants are processed.
        state = [0] * numCourses

        def hasCycle(v):
            if state[v] == 1:
                # This vertex is processed so we pass.
                return False
            if state[v] == -1:
                # This vertex is being processed and it means we have a cycle.
                return True

            # Set state to -1
            state[v] = -1

            for i in adjList[v]:
                if hasCycle(i):
                    return True

            state[v] = 1
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v):
                return False

        return True

"""
Solution 3: DFS with a stack storing all decendants being processed
Same idea as Solution 1, this time we use a stack to store all vertices being processed.
While visiting a descendant of a vertex, if we found it in the stack it means a cycle appears.

This technique is also used to find a Topological order from the graph.

"""
class Solution:
    def buildAdjacencyList(self, n, edgesList):
        ...

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build Adjacency list from Edges list
        adjList = self.buildAdjacencyList(numCourses, prerequisites)
        visited = set()

        def hasCycle(v, stack):
            if v in visited:
                if v in stack:
                    # This vertex is being processed and it means we have a cycle.
                    return True
                # This vertex is processed so we pass
                return False

            # mark this vertex as visited
            visited.add(v)
            # add it to the current stack
            stack.append(v)

            for i in adjList[v]:
                if hasCycle(i, stack):
                    return True

            # once processed, we pop it out of the stack
            stack.pop()
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v, []):
                return False

        return True

"""
Solution 4: BFS with Kahn's algorithm for Topological Sorting
This solution is usually seen in problems where we need to answer two questions:

Is it possible to have a topological order?
if yes then print out one of all the orders.
"""

class Solution:
    def buildAdjacencyList(self, n, edgesList):
                ...

    def topoBFS(self, numNodes, edgesList):
        # Note: for consistency with other solutions above, we keep building
        # an adjacency list here. We can also merge this step with the next step.
        adjList = self.buildAdjacencyList(numNodes, edgesList)

        # 1. A list stores No. of incoming edges of each vertex
        inDegrees = [0] * numNodes
        for v1, v2 in edgesList:
            # v2v1 form a directed edge
            inDegrees[v1] += 1

        # 2. a queue of all vertices with no incoming edge
        # at least one such node must exist in a non-empty acyclic graph
        # vertices in this queue have the same order as the eventual topological
        # sort
        queue = []
        for v in range(numNodes):
            if inDegrees[v] == 0:
                queue.append(v)

        # initialize count of visited vertices
        count = 0
        # an empty list that will contain the final topological order
        topoOrder = []

        while queue:
            # a. pop a vertex from front of queue
            # depending on the order that vertices are removed from queue,
            # a different solution is created
            v = queue.pop(0)
            # b. append it to topoOrder
            topoOrder.append(v)

            # increase count by 1
            count += 1

            # for each descendant of current vertex, reduce its in-degree by 1
            for des in adjList[v]:
                inDegrees[des] -= 1
                # if in-degree becomes 0, add it to queue
                if inDegrees[des] == 0:
                    queue.append(des)

        if count != numNodes:
            return None  # graph has at least one cycle
        else:
            return topoOrder

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return True if self.topoBFS(numCourses, prerequisites) else False