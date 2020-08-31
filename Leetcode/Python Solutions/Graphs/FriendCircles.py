"""
LeetCode Problem: 547. Friend Circles
Link: https://leetcode.com/problems/friend-circles/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ans = 0
        n = len(M)
        visited = [False for i in range(n)]  # Visited array
        
        # Recursive Depth First Search

        def DfsHelper(i, visited, M):
            visited[i] = True   # Mark the current node as visited
            
            # Traverse all of the node's childrens
            for j in range(len(M[0])):
                # Recursively call the function if the node's children are not visited
                if M[i][j] == 1 and visited[j] == False:
                    DfsHelper(j, visited, M)
                    
            return 1  # Returns True since all the nodes in this recursive call belongs to the same SCC
        
        for i in range(n):
            # Recursively call the DFS method if the node is not visited
            if visited[i] == False:
                ans += DfsHelper(i, visited, M)
                
        return ans