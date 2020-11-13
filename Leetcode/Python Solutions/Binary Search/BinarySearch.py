"""
LeetCode Problem 704. Binary Search

Link: https://leetcode.com/problems/binary-search/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(Log N)
Space Complexity: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        low = 0                     # Index of the first element in the array
        high = len(nums) -1         # Index of the last element in the array
        
        
        # Check to see if the target is present in the array
        while low <= high:
            mid = (low+high)//2     # Get the middle index
            
            if nums[mid] == target: # Check if the array at the middle is equal to the target
                return mid
            
            # If the array at the middle is bigger than the target than discard the right side
            elif nums[mid] > target:
                high = mid - 1
            
            # If the array at the middle is smaller than the target than discard the left side
            else:
                low = mid + 1
        
        return -1                   # Return -1 if the target is not present in the array