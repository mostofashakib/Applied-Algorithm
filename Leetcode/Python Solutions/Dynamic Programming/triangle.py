"""
LeetCode Problem: 120. Triangle
Link: https://leetcode.com/problems/triangle/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^2)
Space Complexity: O(N)
"""

# Dynamic Programming - Bottom Up

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for row in range(len(triangle)-1, 0, -1):
            curr_row = triangle[row]
            prev_row = triangle[row-1]
            
            for i in range(len(prev_row)):
                prev_row[i] += min(curr_row[i], curr_row[i+1])
                
        return triangle[0][0]

# Recursion + Memoization - Top Down

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.ans = float('inf')
        
        @lru_cache(maxsize=None)
        def dfs(idx, count, i):
            if i == len(triangle):
                self.ans = min(self.ans, count)
                return
                
            dfs(idx, triangle[i][idx] + count, i + 1)
            dfs(idx+1, triangle[i][idx+1] + count, i + 1)
            
        dfs(0, triangle[0][0], 1)
            
        return self.ans