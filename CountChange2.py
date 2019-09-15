"""
LeetCode Problem: 518. Coin Change 2
Link: https://leetcode.com/problems/coin-change-2/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * amount
        
        for coin in coins:
            for i in range(1, amount+1):
                if i - coin >= 0:
                    dp[i] = dp[i] + dp[i-coin]
        return dp[amount]