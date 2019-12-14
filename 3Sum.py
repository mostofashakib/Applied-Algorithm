"""
LeetCode Problem 15. 3Sum

Link: https://leetcode.com/problems/3sum/
Written by: Mostofa Adib Shakib
Language: Python
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            target = 0 - nums[i]
            while low < high:
                if nums[low] + nums[high] == target:
                    result.add((nums[i], nums[low], nums[high]))
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < target:
                    low += 1
                else:
                    high -= 1
        return list(result)

