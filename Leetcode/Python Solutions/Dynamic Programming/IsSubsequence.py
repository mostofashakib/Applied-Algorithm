"""
LeetCode Problem: 392. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/
Written by: Mostofa Adib Shakib
Language: Python

"""

"""
Recursion + Memoization[Built-in function]
Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""

from functools import lru_cache

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)-1
        m = len(t)-1
        
        @lru_cache               # caching the intermediate results to avoid recomputation
        def helper(s, p, n, m):
            if n < 0 or m < 0:
                return 0
            if s[n] == p[m]:
                return 1 + helper(s, p, n-1, m-1)
            else:
                return max(helper(s, p, n, m-1), helper(s, p, n-1, m))
        
        if n+1 == helper(s, t, n, m): # check if the entire string s exists in t or not
            return True
        else:
            return False

"""
Dynamic Programming
Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s) # column
        m = len(t) # row
        
        dp = [ [0 for i in range(n+1)] for j in range(m+1) ]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        if n == dp[-1][-1]: # check if the entire string s exists in t or not
            return True
        else:
            return False
    


