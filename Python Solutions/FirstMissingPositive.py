"""
LeetCode Problem: 41. First Missing Positive
Link: https://leetcode.com/problems/first-missing-positive/
Written by: Mostofa Adib Shakib
Language: Python
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1   # if the array is empty 
        
        temp = []               # an array that keeps only positive numbers greater than 1
        maximum = max(nums)     # returns the maximum element in the array
        
        for i in nums:
            if i >= 1:
                temp.append(i)   
        
        if len(temp) == 0: return 1   # if the array is empty return 1
                
        if len(temp) == 1:            # if the length of the array is 1 and the element is 1 then return 2 else return 1
            if temp[0] == 1:
                return 2
            else: return 1
        
        temp = sorted(temp)         # sort the temporary array
        
        if temp[0] > 1: return 1    # if the first element of the sorted array is greater than one then return 1
        
        SmallestPositiveNumber = 1   # initializing the current smallest positive number 
                
        for i in range(1,len(temp)):    # loop over every element of the temporary array
            temp1 = abs(temp[i] - temp[i-1])   #find the absolute difference between two numbers 
            if temp1 > 1:                                # if the absolute difference is greater than one then we found the missing integer
                SmallestPositiveNumber = temp[i-1] + 1   # this returns the smallest missing integer.
                return SmallestPositiveNumber
        
        SmallestPositiveNumber = maximum + 1     # if there is no missing integer in the array then the answer is the next biggest element not currently in the array
        
        return SmallestPositiveNumber    # returns the smallest positive missing integer.