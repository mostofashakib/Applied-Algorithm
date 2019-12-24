"""

LeetCode Problem: 322. Coin Change
Link: https://leetcode.com/problems/coin-change/
Language: Python
Written by: Mostofa Adib Shakib

A = Amount to make change
C = Total coins provided

Time complexity: O(A * C)
Space complexity: O(A)

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ float('inf') for i in range(amount+1) ]  # We fill the dp table with default values which stores the answer to our sub problems
        dp[0] = 0 # The answer to making change with minimum coins for 0 will always be 0 coins no matter what the coins we are given are
        
        for coin in coins:  # // For each coin we are given
            for i in range(coin, amount +1): # Solve every subproblem from 1 to amount
                dp[i] = min( dp[i-coin] + 1, dp[i])  # this relation gives us the optimal solution

    # If we do not have an answer then dp[amount] will be amount + 1 and hence dp[amount] > amount will be true. We then return -1. Otherwise, dp[amount] holds the answer

        return dp[-1] if dp[-1] != float('inf') else -1 