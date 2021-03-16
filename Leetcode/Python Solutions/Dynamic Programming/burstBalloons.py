"""
LeetCode Problem: 312. Burst Balloons
Link: https://leetcode.com/problems/burst-balloons/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        nums = [1] + nums + [1]
        dp = [[0]*len(nums) for _ in nums]
        
        for width in range(1, len(nums)-1):
            for left in range(1, len(nums)-width):
                right = left + width
                mult = nums[left-1] * nums[right]
                
                for i in range(left, right):
                    dp[left][right] = max(dp[left][right], nums[i]*mult + dp[left][i] + dp[i+1][right])
                    
        return dp[1][-1]