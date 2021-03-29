"""
LeetCode Problem: 713. Subarray Product Less Than K
Link: https://leetcode.com/problems/subarray-product-less-than-k/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        length = len(nums)
        count = 0
        left = 0
        right = 0
        product = 1
        
        while right < length:
            product *= nums[right]
            
            while product >= k:
                product /= nums[left]
                left += 1
                
            count += (right-left+1)
            right += 1
            
        return count