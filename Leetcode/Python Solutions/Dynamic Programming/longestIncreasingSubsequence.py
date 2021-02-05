"""
LeetCode Problem: 300. Longest Increasing Subsequence
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        
        for index in range(1, length):
            j = 0
            
            while j < index:
                if nums[j] < nums[index]:
                    dp[index] = max(dp[index], dp[j] + 1)
                j += 1
                
        return max(dp)