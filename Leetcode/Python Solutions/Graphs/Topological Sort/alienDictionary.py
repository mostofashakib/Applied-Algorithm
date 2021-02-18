"""
LeetCode Problem: 269. Alien Dictionary
Link: https://leetcode.com/problems/alien-dictionary/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(V + E)
Space Complexity: O(n)
"""

# Solution 1

from collections import defaultdict 

class Solution:
    
    def buildVertices(self, words, vertices):
        visitedChar = set()
        
        for word in words:
            if word not in visitedChar:
                visitedChar.add(word)
                
                for char in word:
                    if char not in vertices:
                        vertices.append(char)
                        
        return vertices
        
    def alienOrder(self, words: List[str]) -> str:
        if len(set(words)) == 1:
            return words[0]
        
        if len(words) == 2 and words[0].startswith(words[1]):
            return ""
        
        vertices = self.buildVertices(words, [])
        graph = defaultdict(list)
        noOfEdges = len(vertices)
        in_degree = {}
        
        for i in vertices:
            in_degree[i] = 0
            
        for i in range(1, len(words)):
            previousWord = words[i-1]
            currentWord = words[i]
            
            length = min(len(previousWord), len(currentWord))
            
            for i in range(length):
                
                if previousWord[i] != currentWord[i]:
                    graph[previousWord[i]].append(currentWord[i])
                    break
        
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

        if count != noOfEdges:
            return ""
        
        else:
            return ''.join(result)

# Solution 2

from collections import defaultdict 

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        
    def addEdges(self, u, v):
        self.graph[u].append(v)
        
    def topSortHelper(self, v, visited, stack):
        visited.add(v)

        for char in self.graph[v]:
            if char not in visited:
                self.topSortHelper(char, visited, stack)

        stack.append(v)
        
    def topSort(self):
        visited = set()
        stack = []
        
        for char in self.vertices:
            if char not in visited:
                self.topSortHelper(char, visited, stack)
                
        return ''.join(stack[::-1])
    
    def isCyclicHelper(self, v, visited, recStack): 
        visited.add(v)
        recStack.add(v)
        
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.isCyclicHelper(neighbour, visited, recStack) == True:
                    return True
                
            elif neighbour in recStack: 
                return True
  
        recStack.remove(v)
    
        return False
  
    def isCyclic(self): 
        visited = set()
        recStack = set()
        
        for node in self.vertices: 
            if node not in visited: 
                if self.isCyclicHelper(node, visited, recStack) == True:
                    return True
        
        return False

class Solution:
    
    def buildVertices(self, words, vertices):
        visitedChar = set()
        
        for word in words:
            if word not in visitedChar:
                visitedChar.add(word)
                
                for char in word:
                    if char not in vertices:
                        vertices.append(char)
                        
        return vertices
        
    def alienOrder(self, words: List[str]) -> str:
        # Edge cases
        if len(set(words)) == 1:
            return words[0]
        
        if len(words) == 2 and words[0].startswith(words[1]):
            return ""
        
        vertices = self.buildVertices(words, [])
                    
        g = Graph(vertices)
        
        for i in range(1, len(words)):
            previousWord = words[i-1]
            currentWord = words[i]
            
            for i in range(len(previousWord)):
                
                if previousWord[i] != currentWord[i]:
                    g.addEdges(previousWord[i], currentWord[i])
                    break
        
        if g.isCyclic() == False:
            return g.topSort()
        else:
            return ""