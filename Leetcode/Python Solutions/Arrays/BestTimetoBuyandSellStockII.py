"""

LeetCode Problem 122. Best Time to Buy and Sell Stock II
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Written by: Mostofa Adib Shakib
Language: Python

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0    # special case
        
        ans = 0
        
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                ans += prices[i] - prices[i-1]
        return ans