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

class  Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE, max3 = Integer.MIN_VALUE;
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:         # n lies between min1 and min2
                min2 = n
            if n >= max1:           # n is greater than max1, max2 and max3
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:         # n lies betweeen max1 and max2
                max3 = max2
                max2 = n
            elif n >= max3          # n lies betwen max2 and max3
                max3 = n

        return max(min1 * min2 * max1, max1 * max2 * max3)

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
