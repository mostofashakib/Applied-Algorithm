"""
LeetCode Problem: 583. Delete Operation for Two Strings
Link: https://leetcode.com/problems/delete-operation-for-two-strings/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(M*N)
Space Complexity: O(M*N)
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
    
        # If either of the words are empty
        if n == 0:
            return m
        
        if m == 0:
            return n

        # Create the dynamic programming table
        
        dp = [ [0 for i in range(m+1)] for j in range(n+1) ]
        
        # Minimum number of deletion needed if the first string is empty

        for r in range(n+1):
            dp[r][0] = r

        # Minimum number of delection needed if the second string is empty
        
        for c in range(m+1):
            dp[0][c] = c

        # If the two characters are a match then we don't need to delete
        # However, if the characters are a mismatch then we need to make at least one deletion
        
        for r in range(1, n+1):
            for c in range(1, m+1):
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r][c-1], dp[r-1][c])

        return dp[-1][-1]