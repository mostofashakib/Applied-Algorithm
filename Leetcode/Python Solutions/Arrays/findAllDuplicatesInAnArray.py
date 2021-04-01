"""
LeetCode Problem: 442. Find All Duplicates in an Array
Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
                
        for i in range(length):
            index = abs(nums[i]) - 1        # To prevent going out of bound
            
            if nums[index] < 0:
                result.append(index + 1)    # Push the correct index
            else:
                nums[index] = -nums[index]  # Helps to keep track if a number has previously been visited
        
        return result