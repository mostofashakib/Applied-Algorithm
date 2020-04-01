"""
LeetCode Problem: 26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity : O(n)
Space complexity : O(1).
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # edge cases 
        
        if not nums: return 0
        if len(nums) == 1: return 1
        
        temp = nums[0]
        i = 1
        length = len(nums)
        
        
        while i < length:
            if nums[i] != temp:
                temp = nums[i]
                i += 1
            else:
                del nums[i-1]
                temp = nums[i-1]
                length -= 1
        
        return len(nums)
