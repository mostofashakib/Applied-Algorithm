"""
LeetCode Problem 153. Find Minimum in Rotated Sorted Array

Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Written by: Mostofa Adib Shakib
Language: Python

Time complexity: O(log n)
Space complexity: O(1)
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # handling edge cases
        if not nums: return -1                   # if array is empty no elements exits
        if len(nums) == 1: return nums[0]        
        if len(nums) == 2: return nums[0] if nums[0] < nums[1] else nums[1]
        if nums[0] < nums[-1]: return nums[0]   # check if the array is already sorted in ascending order
        
        low, high = 0, len(nums) -1
        
        while low <= high:
            mid = (low+high)//2
            if nums[mid] > nums[low] and nums[low] > nums[high]:
                low = mid
            elif nums[mid] < nums[high] and nums[low] > nums[high]:
                high = mid
            elif nums[mid] <= nums[high] or nums[mid] >= nums[high]:
                return nums[mid] if mid != low else nums[high]