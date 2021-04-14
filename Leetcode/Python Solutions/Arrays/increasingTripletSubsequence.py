"""
LeetCode Problem: 334. Increasing Triplet Subsequence
Link: https://leetcode.com/problems/increasing-triplet-subsequence/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)
        firstNumber = float('inf')
        secondNumber = float('inf')
        
        for num in nums:
            if num <= firstNumber:
                firstNumber = num
                
            elif num <= secondNumber:
                secondNumber = num
            else:
                return True
        
        return False