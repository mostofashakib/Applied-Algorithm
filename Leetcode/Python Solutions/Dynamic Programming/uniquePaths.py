"""
LeetCode Problem: 62. Unique Paths
Link: https://leetcode.com/problems/unique-paths/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Recursion + Memoization
# Time Complexity: O(M*N)
# Space Complexity: O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(m, n):
            if m == 1 or n == 1:
                return 1

            return dfs(m - 1, n) + dfs(m, n - 1)
        
        return dfs(m, n)

# Dynamic Programming
# Time Complexity: O(M*N)
# Space Complexity: O(M*N)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]
        
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[-1][-1]