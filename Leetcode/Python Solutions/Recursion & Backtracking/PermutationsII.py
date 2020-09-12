"""
LeetCode Problem: 47. Permutations II
Link: https://leetcode.com/problems/permutations-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n!)
Space Complexity: O(1)
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # A recursive function that generates all the permutations of an array
        def recursiveHelper(index):

            # Checks if the length of the index is equal to the length of the array
            if index == len(nums) - 1:
                current_permutation = nums.copy()                       # Creates a shallow copy of the current array
                current_permutationTuple = tuple(current_permutation)   # Converts the list to a tuple

                if current_permutationTuple not in visited:             # Checks if the tuple exits in the set or not
                    visited.add(current_permutationTuple)               # Adds the tuple to the set
                    result.append(current_permutation)                  # Adds the current array to the result array
            else:
                # Finds all the possible permutations for each index
                for j in range(index, len(nums)):
                    nums[index], nums[j] = nums[j], nums[index]         # Swaps the positions
                    recursiveHelper(index+1)                            # Recursively calls the next index
                    nums[index], nums[j] = nums[j], nums[index]         # Backtrack
                    
        result = []                                                     # Result array
        visited = set()                                                 # Initializing the visited set
        recursiveHelper(0)                                              # Calls the recursive function
        return Result                                                   # Returns the result