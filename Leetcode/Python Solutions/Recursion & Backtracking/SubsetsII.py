"""
LeetCode Problem: 90. Subsets II
Link: https://leetcode.com/problems/subsets-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n*2^n)
Space Complexity: O(n*2^n)
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def recursiveHelper(index, current):
            currentTuple = tuple(current.copy())    # Converts the list to a tuple
            if currentTuple not in visited:
                visited.add(currentTuple)           # Adds the tuple to the visited set
                result.append(current.copy())       # Creates a shallow copy of the current array and appends to the result array
            for j in range(index, len(nums)):
                current.append(nums[j])             # Push the value at the current index to the current array
                recursiveHelper(j+1, current)       # Recursively call the next index
                current.pop()                       # Backtrack
        
        nums = sorted(nums)                         # Sort the array
        result = []                                 # Keeps track of the result
        visited = set()                             # Initializing the visited set
        recursiveHelper(0, [])                      # Calls the recursive function
        return result                               # Returns the answer