"""
LeetCode Problem: 16. 3Sum Closest
Link: https://leetcode.com/problems/3sum-closest/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^2)
Space Complexity: O(logN)
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            
            while low < high:
                currentSum = nums[i] + nums[low] + nums[high]
                
                if abs(currentSum-target) < abs(diff):
                    diff = target - currentSum
                
                if currentSum < target:
                    low += 1
                else:
                    high -= 1
                    
            if diff == 0:
                break
        
        return target-diff