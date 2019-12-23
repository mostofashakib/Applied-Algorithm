"""
LeetCode Problem: 343. Integer Break
Link: https://leetcode.com/problems/integer-break/
Written by: Mostofa Adib Shakib
Language: Python


Intuition:

We can assume that the volume of the knapsack is n. The items we can choose range from 1 to n - 1(because we must divide n into at least two positive parts).
The point is that we can choose each item many times.
    The first loop means the items we can choose(i means first i items).
    And in the second loop, j means the sum of items that we are going to choose.
    For each item, we have two choices, pick it up or not. And we should choose the max result.
    just as tmp = max(tmp, dp[j] * (i-j), j * (i-j))

"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        
        dp = [0, 1, 1]
        
        for i in range(3, n+1):
            tmp = 1
            for j in range(1, i):
                tmp = max(tmp, dp[j] * (i-j), j * (i-j))
            dp.append(tmp)
        
        return dp[-1]

