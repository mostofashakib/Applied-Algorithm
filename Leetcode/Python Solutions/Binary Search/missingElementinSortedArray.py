"""
LeetCode Problem 1060. Missing Element in Sorted Array

Link: https://leetcode.com/problems/missing-element-in-sorted-array/
Written by: Mostofa Adib Shakib
Language: Python
"""

# Binary Search
# Time Complexity: O(logn)
# Space complexity: O(n)

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        hashSet = set(nums)
        minimum = nums[0]
        maximum = nums[-1]
        low = 0
        high = len(nums) - 1
        count = k
        
        # This is true when the missing number is outside the array
        if (maximum-minimum) - (len(nums)-1) < k:
            return nums[-1] + k - ( (maximum-minimum) - (len(nums)-1) )
        
        # Binary Search to narrow down the search space
        while count > 0:
            mid = (low+high)//2                 # Calculate the mid point
            actualIndex = nums[mid] - minimum   # find out the actual index of a number
            indexDiff = actualIndex - mid       # calculate the index difference
            
            if (k-indexDiff) > 0:
                k -= indexDiff
                
            if indexDiff == k:
                break
            
            elif indexDiff < count:
                low = mid
                count -= indexDiff
            else:
                high = mid
                count -= indexDiff
        
        # Linear scan on the narrow change
        for i in range(nums[low], nums[high]):
            if i not in hashSet:
                k -= 1
            
            if k == 0:
                return i

# Brute Force
# Time Complexity: O(n)
# Space complexity: O(n)

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        hashSet = set(nums)
        minimum = nums[0]
        maximum = nums[-1]
        count = 0
        
        for i in range(minimum, maximum+1):
            if i not in hashSet:
                count += 1
            
            if count == k:
                return i
            
        return nums[-1] + (k-count)