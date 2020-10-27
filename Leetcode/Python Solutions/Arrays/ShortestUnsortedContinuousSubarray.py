"""
LeetCode Problem: 581. Shortest Unsorted Continuous Subarray
Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Time complexity : O(nlogn)
# Space complexity : O(1)

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums) # Sorts an array in ascending order

        if sortedNums == nums: # Returns 0 if the array is already sorted
            return 0

        count = float('inf')
        length = len(nums)
        i = 0
        index = 0
        flag = False          # A flag that checks have we seen the first occurence of mismatch or not
        lastIndex = 0       # Keeps track of the index of the last occurence of mismatch
        
        # Precompute the index of the last occurence of mismatch
        for i in range(length):
            if flag == False and sortedNums[i] != nums[i]:
                flag = True
            elif sortedNums[i] != nums[i]:
                lastIndex = i

        while index < length:
            if sortedNums[index] != nums[index]:
                return (lastIndex-index+1)
            index += 1


# Time complexity : O(nlogn)
# Space complexity : O(n)

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)       # Sorts an array in ascending order
        
        if sortedNums == nums:          # Returns 0 if the array is already sorted
            return 0
        
        length = len(nums)
        i = 0
        index = 0
        hashmap = {}
        flag = False                    # A flag that checks have we seen the first occurence of mismatch or not
        first = 0                       # Keeps track of the index of the first occurence of mismatch
        
        # maps the first occurence of mismatch with the last-most occurence of mismatch
        for i in range(length):
            if flag == False and sortedNums[i] != nums[i]:
                flag = True
                first = i
            elif sortedNums[i] != nums[i]:
                hashmap[first] = i
        
        while index < length:
            if sortedNums[index] != nums[index]:
                return (hashmap[index]-index+1)
            index += 1