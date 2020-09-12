"""
LeetCode Problem: 78. Subsets
Link: https://leetcode.com/problems/subsets/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n*2^n)
Space Complexity: O(n*2^n)
"""

# Solution 1

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def recursiveHelper(index, current):
            # Creates a shallow copy of the current array and appends to the result array
            result.append(current.copy())
            
            for j in range(index, len(nums)):
                current.append(nums[j])         # push the value at the current index to the current array
                recursiveHelper(j+1, current)   # Recursively call the next index
                current.pop()                   # Backtrack
                    
        result = []                             # Keeps track of the result
        recursiveHelper(0, [])                  # Calls the recursive function
        return result                           # Returns the answer

# Solution 2

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def recursiveHelper(index, current):
            # Base case
            if index == len(nums):
                result.append(current)                              # Append current to the result array
            else:                
                recursiveHelper(index+1, current)                   # If the element is not selected
                recursiveHelper(index+1, current + [nums[index]])   # if the element is selected

        result = []                                                 # Keeps track of the result
        recursiveHelper(0, [])                                      # Calls the recursive function
        return result                                               # Returns the answer