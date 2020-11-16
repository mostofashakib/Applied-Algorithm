"""
LeetCode Problem: 264. Ugly Number II
Link: https://leetcode.com/problems/ugly-number-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Compplexity: O(1)  # Time is constant because we only loop 1689 times
Space Complexity: O(n)
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initializing the dynamic programming table. First first ugly number is the base condition
        dp = [1] + [0] * 1689
        # Initializing the iterators
        iteratorTwo = iteratorThree = iteratorFive = 0
        
        for i in range(1, 1690):
            # Select the ugly number at the ith index
            dp[i] = min(dp[iteratorTwo]*2, dp[iteratorThree]*3, dp[iteratorFive]*5)
            
            # If the next ugly ugly is the next multiple of 2 then increment 2's iterator
            if dp[i] == dp[iteratorTwo]*2:
                iteratorTwo += 1
            
            # If the next ugly ugly is the next multiple of 3 then increment 3's iterator
            if dp[i] == dp[iteratorThree]*3:
                iteratorThree += 1
            
            # If the next ugly ugly is the next multiple of 5 then increment 5's iterator
            if dp[i] == dp[iteratorFive]*5:
                iteratorFive += 1
            
        return dp[n-1]      # Return the nth ugly number