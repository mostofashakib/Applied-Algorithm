"""
LeetCode Problem 525. Contiguous Array
Link: https://leetcode.com/problems/contiguous-array/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {}
        hashmap[0] = -1
        maximum = 0
        counter = 0
        
        for index in range(len(nums)):
            if nums[index] == 0:
                counter -= 1
            else:
                counter += 1
            
            if counter not in hashmap:
                hashmap[counter] = index
            else:
                maximum = max(maximum, index - hashmap[counter])
        
        return maximum