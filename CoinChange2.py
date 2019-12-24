"""
LeetCode Problem: 518. Coin Change 2
Link: https://leetcode.com/problems/coin-change-2/
Language: Python
Written by: Mostofa Adib Shakib

A is the amount to make change for.
n is the total denominations avaliable to us.

Time complexity: O( A * n )
For each denomination we will be solving A subproblems. So for each of the n we will be doing A work, hence multiplication.

Space complexity: O( A * n )


Strategy:

Add coins one-by-one, starting from base case "no coins".

For each added coin, compute recursively the number of combinations for each amount of money from 0 to amount.

Algorithm

    Initiate number of combinations array with the base case "no coins": dp[0] = 1, and all the rest = 0.

    Loop over all coins:

    For each coin, loop over all amounts from 0 to amount:

    For each amount x, compute the number of combinations: dp[x] += dp[x - coin].
    
    Return dp[amount].

"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)  # Holds the answer to all subproblems.
        dp[0] = 1 #  max ways to make change for 0 will be 1, doing nothing.
        
        for coin in coins:
            for i in range(1, amount+1):  # Set the subproblem for the amount of 0 to 1 when solving this row
                if i - coin >= 0:
                    dp[i] = dp[i] + dp[i-coin] # dp[i] will be the sum of the ways to make change not considering this coin dp[i] and the ways to make change considering this coin dp[i - currentCoinValue]
        return dp[amount]