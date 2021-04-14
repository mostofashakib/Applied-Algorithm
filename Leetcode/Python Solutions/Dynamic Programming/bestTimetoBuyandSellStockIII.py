"""
LeetCode Problem: 123. Best Time to Buy and Sell Stock III
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Video Explanation: 
    https://www.youtube.com/watch?v=Pw6lrYANjz4
    https://www.youtube.com/watch?v=oDhu5uGq_ic&t=1013s
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp = [ [0 for d in prices] for t in range(3) ]
        length = len(prices)
        
        for t in range(1, 3):
            maxSoFar = float('-inf')
            
            for d in range(1, length):
                maxSoFar = max(maxSoFar, dp[t-1][d-1] - prices[d-1])
                dp[t][d] = max(dp[t][d-1], maxSoFar + prices[d])
                
        return dp[-1][-1]