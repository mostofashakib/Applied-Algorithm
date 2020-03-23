"""
LeetCode Problem: 215. Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort(reverse=True)
        count = 0
        for i in range(k):
            count = nums[i]
        return count