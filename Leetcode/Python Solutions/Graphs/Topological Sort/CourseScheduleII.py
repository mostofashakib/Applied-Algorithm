"""
LeetCode Problem: 210. Course Schedule II
Link: https://leetcode.com/problems/course-schedule-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(V+E)
Space Complexity: O(V)
"""

# Kahn's Topological Sort Algorithm

from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # building up the DAG
        
        for curCourse, prevCourse in prerequisites:
            self.addEdge(prevCourse, curCourse)
        
        # initializing the in_degree array
        
        in_degrees = [0] * numCourses
        
        # finding the number of incoming edges for every vertices
        
        for i in self.graph:
            for j in self.graph[i]:
                in_degrees[j] += 1
        
        # a queue to track the next vertex to be processed
        
        queue = []
        
        # finding the initial batch of vertex which has 0 incoming nodes
        
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
                
        result = []   # stores the resulting topological sort
        count = 0     # keeps count of the number of visited vertices
        
        while queue:
            u = queue.pop(0)   # pops the first vertex from the queue
            result.append(u)   # appends the vertex to the result array
            
            # traverses all the neighbors and decrements their incoming edges by 1
            
            for i in self.graph[u]:
                in_degrees[i] -= 1
                if in_degrees[i] == 0:
                    queue.append(i) # pushes the neighboring vertex if their no. of incoming edges is 0
            count += 1 # increments the visited vertices count by 1
            
            
        if count != numCourses: # if the graph contains a cycle then it is not possible to take n courses
            return []
        else:
            return result