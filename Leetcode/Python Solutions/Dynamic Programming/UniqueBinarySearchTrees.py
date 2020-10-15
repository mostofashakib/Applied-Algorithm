"""
LeetCode Problem: 96. Unique Binary Search Trees
Link: https://leetcode.com/problems/unique-binary-search-trees/
Video Link: https://www.youtube.com/watch?v=CMaZ69P1bAc
Resources: https://en.wikipedia.org/wiki/Catalan_number

Written by: Mostofa Adib Shakib
Language: Python

For Catalan(3)

        Catalan(2)
        /        \
   Catalan(1)   Catalan(1)
     (LST)        (RST)

LeftSubTree(LST): Value increases upto the given catalan number
RightSubTree(RST): Value decreases until 0
"""

# Dynamic Programming
# Time Complexity: O(n*m)
# Space Complexity: O(n)


class Solution:
    def numTrees(self, n: int) -> int:
        # Assume the 0th case
        # The catalan number for Catalan(1) = 1

        dp = [1, 1] + [0] * (n-1)

        for i in range(2, n+1):                     # The outer loop makes every number the root and calculates it's catalan number
            for j in range(1, i+1):                 # The inner calculates the summation of the cartesian product for the given catalan number
                dp[i] += dp[j-1] * dp[i-j]          # The left value increases where as the right value decreases
                
        return dp[-1]