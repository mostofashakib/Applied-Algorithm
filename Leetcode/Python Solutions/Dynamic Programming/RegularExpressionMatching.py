"""
LeetCode Problem: 10. Regular Expression Matching
Link: https://leetcode.com/problems/regular-expression-matching/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
# m = length of the pattern string
# n = length of the text string

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s) # row
        m = len(p) # column
        
        dp = [ [False for i in range(m+1)] for j in range(n+1) ]
        
        # Two empty strings are always a match
        dp[0][0] = True
        
        # this is for the 0th row
        # if we encounter a kleene star then look at two cells to the right
        # this is because a* or a*b* is also equivalent to the empty string
        
        for i in range(1, m+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                # if the characters are either a direct match or if the character is a '.'
                # this is because if the cell substring without the matching character
                # is also a match then the entire string is a match
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1] # look at the cell diagonally above
                # if we encounter a kleene star
                elif p[j-1] == '*':
                    # check of the 0th occurance of the number:
                    dp[i][j] = dp[i][j-2]
                    # check for the n+ occurance if and only if the previous character is a match
                    # or if the previous character is a wild card character '.'
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        # if this condition is true then look at the cell directly above
                        # or look at the cell two steps to the left. If their of the cell is True then it's a match
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                else:
                    # if the chracter is a miss match
                    dp[i][j] = False
                    
        return dp[-1][-1]