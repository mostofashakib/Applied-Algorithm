"""
LeetCode Problem: 724. Find Pivot Index
Link: https://leetcode.com/problems/find-pivot-index/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 

S as the sum of the numbers, and we are at index i. If we knew the sum of numbers leftsum that are to the left of index i,
then the other sum to the right of the index would just be S - nums[i] - leftsum.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) <= 2: return -1
        
        leftSum = 0
        totalSum = sum(nums)
        
        for index, value in enumerate(nums):
            if leftSum == (totalSum - leftSum - value):
                return index
            leftSum += value
                    
        return -1