"""
LeetCode Problem: 1480. Running Sum of 1d Array
Link: https://leetcode.com/problems/running-sum-of-1d-array/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums