"""
LeetCode Problem: 322. Coin Change
Link: https://leetcode.com/problems/coin-change/
Reading Material: https://www.geeksforgeeks.org/coin-change-dp-7/
Language: Python
Written by: Mostofa Adib Shakib

A = Amount to make change
C = Total coins provided

Time complexity: O(A * C)
Space complexity: O(A)

What is the magic number beyond which you can always take the highest denominations?
Take the LCM of all the elements in the coins array

Example 1:
coins = [25, 10, 5, 1]
Answer: 50

Example 2:
coins = [89, 26, 1]
Answer: 6942 
"""

# Dynamic Programming
# Time Complexity: O(n*m)
# Space Complexity: O(n)

def coinChange(coins, total, n):
	# Initializing the dynamic programming table
	dp = [ [0 for i in range(total+1)] for j in range(n) ]

	for coin in range(n):
		for current_total in range(1, total+1):
			if coin == 0:
				dp[coin][current_total] = (1 + dp[coin][current_total-coins[coin]]) if current_total >= coins[coin] else 0
			elif current_total < coins[coin]:
				# If the current_total is less than the value of the coin
				dp[coin][current_total] = dp[coin-1][current_total]
			else:
				dp[coin][current_total] = min(dp[coin-1][current_total], 1 + dp[coin][current_total-coins[coin]])
	return dp[-1][-1]

# Dynamic Programming - Optimized Space
# Time Complexity: O(n*m)
# Space Complexity: O(n)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ float('inf') for i in range(amount+1) ]  # We fill the dp table with default values which stores the answer to our sub problems
        dp[0] = 0 # The answer to making change with minimum coins for 0 will always be 0 coins no matter what the coins we are given are
        
        for coin in coins:  # // For each coin we are given
            for i in range(coin, amount +1): # Solve every subproblem from 1 to amount
                dp[i] = min( dp[i-coin] + 1, dp[i])  # this relation gives us the optimal solution

    # If we do not have an answer then dp[amount] will be amount + 1 and hence dp[amount] > amount will be true. We then return -1. Otherwise, dp[amount] holds the answer
        return dp[-1] if dp[-1] != float('inf') else -1 