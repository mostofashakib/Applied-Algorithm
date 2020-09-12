"""
LeetCode Problem: 746. Min Cost Climbing Stairs
Link: https://leetcode.com/problems/min-cost-climbing-stairs/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)                  # Add 0 to the cost array this cell will hold the answer
        
        n = len(cost)                   # Calculates the length of the cost array
        
        dp = [0 for i in range(n)]      # Initializing DP table

        # Base cases
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Loop over the array        
        for i in range(2, n):
            # Find the minimum cost to get to a certain cell with the given constaints
            dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i])
            
        return dp[-1]                   # Returns the answer