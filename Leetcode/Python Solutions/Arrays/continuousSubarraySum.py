"""
LeetCode Problem: 523. Continuous Subarray Sum
Link: https://leetcode.com/problems/continuous-subarray-sum/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # Edge Cases
        if n < 2:
            return False
        
        if k == 0:
            for i in range(n - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
                
            return False
        
        for i in range(n):
            currentSum = nums[i]
            
            for j in range(i+1, n):
                currentSum += nums[j]
                
                if currentSum % k == 0:
                    return True
        
        return False