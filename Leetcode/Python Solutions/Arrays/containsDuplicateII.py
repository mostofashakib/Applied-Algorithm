"""
LeetCode Problem 219. Contains Duplicate II
Link: https://leetcode.com/problems/contains-duplicate-ii/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Initializing a hashmap
        hashmap = {}
        
        # Iterate over the array
        for index in range(len(nums)):
            # accessing the number from the array
            number = nums[index]
            
            # check to see if the number exists in the hashmap or not
            if number not in hashmap:
                hashmap[number] = index
            else:
                # if the number doesn't exist in the hashmap then check if the difference between two integers is at most k.
                if index - hashmap[number] <= k:
                    return True
                # update the indicies
                else:
                    hashmap[number] = index
        
        return False