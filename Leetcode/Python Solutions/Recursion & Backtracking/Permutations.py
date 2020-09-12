"""
LeetCode Problem: 46. Permutations
Link: https://leetcode.com/problems/permutations/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n!)
Space Complexity: O(n)
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # A recursive function that generates all the permutations of an array
        def recursiveHelper(index):

            # Checks if the length of the index is equal to the length of the array
            if index == len(nums)-1:
                currentPermutations = nums.copy()       # Creates a shallow copy of the current array
                result.append(currentPermutations)      # Appends the answer to the result array
            else:
                # Finds all the possible permutations for each index
                for j in range(index, len(nums)):
                    nums[index], nums[j] = nums[j], nums[index]         # Swaps the positions
                    recursiveHelper(index+1)                            # Recursively calls the next index
                    nums[index], nums[j] = nums[j], nums[index]         # Backtrack
        
        result = []             # Resultant array
        recursiveHelper(0)      # Calls the recursive function
        return Resultant        # Returns the result