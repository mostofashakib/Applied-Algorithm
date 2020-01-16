"""
LeetCode Problem: 162. Find Peak Element
Link: https://leetcode.com/problems/find-peak-element/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2: return 0
        
        if len(nums) == 2:
            if nums[1] > nums[0]:
                return 1
            else:
                return 0
        
        low = 0
        high = len(nums) -1
        
        while low < high:
            mid = int( (low+high)/2 )
            
            if nums[mid] < nums[mid+1]:
                low = mid +1
            elif nums[mid] < nums[mid-1]:
                high = mid -1
            elif nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
        return low