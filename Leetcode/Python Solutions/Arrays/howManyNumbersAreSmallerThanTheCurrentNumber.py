"""
LeetCode Problem: 1365. How Many Numbers Are Smaller Than the Current Number
Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []                 # keeps track of result
        hashMap = {}                # keeps track of the firstOccurance of a number in a sorted array
        sortedNums = sorted(nums)   # sorts the array in ascending order
        length = len(nums)          # calculates the length of the array
        
        # Populating the hashMap
        for i in range(length):
            number = sortedNums[i]
            
            if number not in hashMap:
                hashMap[number] = i
        
        # Extract the count and put them in the correct order
        for i in range(length):
            number = nums[i]
            result.append(hashMap[number])
        
        return result