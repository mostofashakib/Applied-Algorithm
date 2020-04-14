"""
LeetCode Problem 628. Maximum Product of Three Numbers
Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
Approach 1
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Initializing necessary variables
        
        min1 = float('inf')
        min2 = float('inf')
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        
        for i in nums:
            if i <= min1:       # The number is less than the current minimum value
                min2 = min1
                min1 = i
            elif i <= min2:     # The number is between min1 and min2
                min2 = i
                
            if i >= max1:       # The number is greather than the current maximum value
                max3 = max2
                max2 = max1
                max1 = i
                
            elif i >= max2:     # The number is between max2 and max1
                max3 = max2
                max2 = i
                
            elif i >= max3:     # The number is between max3 and max2
                max3 = i
        
        
        maximum1  = min1*min2 *max1       # If the first two elements have the highest absolute value
        maximunm2 = max1*max2*max3
        
        return max(maximum1, maximunm2)   # The maximum of the two choices

"""
Approach 2: Faster
Time Complexity: O(nlogn)
Space Complexity: O(logn)
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        if len(nums) < 3: return 0
        
        nums = sorted(nums)
        
        def helper(x,y,z):
            return x*y*z
        
        return max(helper(nums[-3], nums[-2], nums[-1]), helper(nums[0], nums[1], nums[-1]))


"""
Approach 3: Slower
Time Complexity: O(nlogn)
Space Complexity: O(logn)
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        
        nums = sorted(nums)
        
        def helper(x,y,z):
            return x*y*z
        
        maximum = nums[-1]
        ans = float('-inf')
        
        for i in range(2, len(nums)):
            ans = max(ans, helper(nums[i-2], nums[i-1], maximum))

        return ans
