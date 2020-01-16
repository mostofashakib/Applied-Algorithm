"""
LeetCode Problem: 198. House Robber
Link: https://leetcode.com/problems/house-robber/
Written by: Mostofa Adib Shakib
Language: Python
Time Complexity: O(n)
Space Complexity: O(1)

Dynamic Programming

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0

		# assume we either start robbing from 0th (which doesn't exist) house or first house
        n = len(nums)
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = nums[0]
        
		# Here we get the maximum of
		# current_house + last_house_robbed - 1  house OR last_house_robbed
		# and add the maximum one to our result
        for i in range(1, n):
            dp[i+1] = max(dp[i], (dp[i-1] + nums[i]) )
            
		# return the last element in result because that's the maximum possible
        return dp[-1]