"""
LeetCode Problem 152. Maximum Product Subarray
Link: https://leetcode.com/problems/maximum-product-subarray/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0               #  special case
        if len(nums) == 1: return nums[0]   #  special case
        
        MaximumProduct = float('-inf')
        MaximumProductSeenSofar = nums[0]
        
        # traverse from the start
        
        for i in range(1, len(nums)):
            
            if nums[i-1] == 0:                # if the previous number is 0 forcefully make it positive
                MaximumProductSeenSofar = 1
            
            MaximumProductSeenSofar = MaximumProductSeenSofar * nums[i]
            
            MaximumProduct = max(MaximumProductSeenSofar, MaximumProduct, nums[i])
            
        MaximumProductSeenSofar = nums[len(nums) -1]
        
        # traverse from the back
        
        for i in range(len(nums)-2, -1, -1):
            
            if nums[i+1] == 0:                # if the previous number is 0 forcefully make it positive
                MaximumProductSeenSofar = 1
            
            MaximumProductSeenSofar = MaximumProductSeenSofar * nums[i]
            
            MaximumProduct = max(MaximumProductSeenSofar, MaximumProduct, nums[i])
        
        return MaximumProduct