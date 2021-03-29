"""
LeetCode Problem: 503. Next Greater Element II
Link: https://leetcode.com/problems/next-greater-element-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [-1] * length
        stack = []
        
        for i in range(length*2):
            # If the number at the previous index is smaller than the current number then update the result array
            while stack and nums[stack[-1]] < nums[i % length]:
                result[stack.pop()] = nums[i % length]
            
            if i < length:
                stack.append(i)
            
        return result