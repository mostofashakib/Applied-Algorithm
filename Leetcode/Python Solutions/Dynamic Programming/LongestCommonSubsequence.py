"""
LeetCode Problem: 1143. Longest Common Subsequence
Link: https://leetcode.com/problems/longest-common-subsequence/
Written by: Mostofa Adib Shakib
Language: Python

"""


"""
Recursive solution - Inefficient
Time Complexity: O(2^n)
Space Complexity: O(1)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        if text1[-1] == text2[-1]:
            text1 = text1[:-1]
            text2 = text2[:-1]
            return 1 + self.longestCommonSubsequence(text1, text2)
        else:
            return max(self.longestCommonSubsequence(text1, text2[:-1]), self.longestCommonSubsequence(text1[:-1], text2))

"""
Recursive + Memoization
Time Complexity: O(m⋅n^2)
Space Complexity: O(m⋅n)
Number of subproblems: M⋅N subproblems
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        def lcs(s, p, n, m):
            if n < 0 or m <0:
                return 0
            if (s, p, n, m) in memo:
                return memo[(s, p, n, m)]
            elif s[n] == p[m]:
                memo[(s, p, n, m)] = 1 + lcs(s, p, n-1, m-1)
            else:
                temp1 = lcs(s, p, n, m-1)
                temp2 = lcs(s, p, n-1, m)
                memo[(s, p, n, m)] = max(temp1, temp2)
            return memo[(s, p, n, m)] 

        return lcs(text1, text2, len(text1)-1, len(text2)-1)

"""
Recursive + Memoization using decorators
Time Complexity: O(m⋅n)
Space Complexity: O(m⋅n)
Number of subproblems: M⋅N subproblems
"""

from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1) - 1
        m = len(text2) - 1
        
        @lru_cache(maxsize=None)
        def lcs(s, p, n, m):
            if n < 0 or m <0:
                return 0
            if s[n] == p[m]:
                result = 1 + lcs(s, p, n-1, m-1)
            else:
                temp1 = lcs(s, p, n, m-1)
                temp2 = lcs(s, p, n-1, m)
                result = max(temp1, temp2)
            return result
            
        return lcs(text1, text2, n, m)

"""
Dynamic Programming
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        
        n = len(text1)
        m = len(text2)

        dp= [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(0, n):
            for j in range(0, m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[-1][-1]
    


