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
    


