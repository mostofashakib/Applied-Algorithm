"""
LeetCode Problem: 121. Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Written by: Mostofa Adib Shakib
Language: Python

Dynamic Programming

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        
        minPrice = float('inf')    # keeps track of the last min found
        maxProfit = 0              # maximum profit seen so far
        n = len(prices)
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, (prices[i] - minPrice))
        
        return maxProfit          # returns the maxmimum profit