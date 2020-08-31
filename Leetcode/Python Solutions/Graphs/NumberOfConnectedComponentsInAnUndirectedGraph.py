"""
LeetCode Problem: 323. Number of Connected Components in an Undirected Graph
Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacent_matrix = [ [] for i in range(n) ]    # Adjacency matrix
        visited = [False for i in range(n)]           # Visited array
        ans = 0
        
        # Building up the adjacency matrix

        for i in edges:
            first = i[0]
            second = i[1]
            
            adjacent_matrix[first].append(second)
            adjacent_matrix[second].append(first)
        
        # Recursive Depth First Search

        def DFSUtil(v, visited, adjacent_matrix):
            visited[v] = True   # Mark the current node as visited
            
            # Traverse all of the node's childrens
            for i in adjacent_matrix[v]:
                # Recursively call the function if the node's children are not visited
                if visited[i] == False:
                    DFSUtil(i, visited, adjacent_matrix)
                    
            return 1   # Returns True since all the nodes in this recursive call belongs to the same SCC
        
        # Traverse through the Adjacency matrix

        for i in range(n):
            # Recursively call the DFS method if the node is not visited
            if visited[i] == False:
                ans += DFSUtil(i, visited, adjacent_matrix)

        return ans