"""
LeetCode Problem: 329. Longest Increasing Path in a Matrix
Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity : O(m*n)
Space complexity : O(m*n)
"""

from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        
        @lru_cache(maxsize=None)   # Python build-in memoization method
        def dfs(i, j):
            m = 0
            if i > 0 and matrix[i-1][j] > matrix[i][j]:
                m = max(m, dfs(i-1, j))
            if j > 0 and matrix[i][j-1] > matrix[i][j]:
                m = max(m, dfs(i, j-1))
            if i < len(matrix)-1 and matrix[i+1][j] > matrix[i][j]:
                m = max(m, dfs(i+1, j))
            if j < len(matrix[0])-1 and matrix[i][j+1] > matrix[i][j]:
                m = max(m, dfs(i, j+1))
            return 1 + m
        
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, dfs(i, j))
                
        return result