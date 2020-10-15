"""
LeetCode Problem: 516. Longest Palindromic Subsequence
Link: https://leetcode.com/problems/longest-palindromic-subsequence/
Written by: Mostofa Adib Shakib
Language: Python
"""

""" Recursion + Memoization

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)-1                                        # Gets the index of the last character
        
        @lru_cache(maxsize=None)
        def helper(i ,j):
            if i == j:                                      # This happens if and only if the string has one character left to look at
                return 1
            elif s[i] == s[j]:                              # Check to see if the characters match or not
                if i+1 == j:                                # Check to make sure i and j remains inside the bounds
                    return 2
                else:
                    return 2 + helper(i+1, j-1)             # Add 2 and recurse without those characters
            else:
                return max(helper(i+1, j), helper(i, j-1))  # If the characters don't match remove a character from each side one at a time and recurse
            
        return helper(0, n)


# Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        string = s[::-1]                                        # Reverse the string
        n = len(s)
        
        dp = [ [0 for i in range(n+1)] for j in range(n+1) ]    # Initializes a DP table
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == string[j-1]:                       # If the characters match then add one to the diagonal cell
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])      # If the characters do not match take the maximum of the adjacent cells
                    
        return dp[-1][-1]