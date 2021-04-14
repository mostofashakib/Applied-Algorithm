"""
LeetCode Problem: 188. Best Time to Buy and Sell Stock IV
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Video Explanation: 
    https://www.youtube.com/watch?v=Pw6lrYANjz4
    https://www.youtube.com/watch?v=oDhu5uGq_ic&t=1013s
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NK)
Space Complexity: O(NK)
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        
        dp = [ [0 for d in prices] for t in range(k+1) ]
        length = len(prices)
        
        for t in range(1, k+1):
            maxSoFar = float('-inf')
            
            for d in range(1, length):
                maxSoFar = max(maxSoFar, dp[t-1][d-1] - prices[d-1])
                dp[t][d] = max(dp[t][d-1], maxSoFar + prices[d])
                
        return dp[-1][-1] 