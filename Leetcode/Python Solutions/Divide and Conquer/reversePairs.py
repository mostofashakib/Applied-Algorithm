"""
LeetCode Problem: 493. Reverse Pairs
Link: https://leetcode.com/problems/reverse-pairs/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        mid = len(nums)//2
        
        count = 0
        
        count += self.reversePairs(nums[:mid])
        count += self.reversePairs(nums[mid:])
        
        nums = sorted(nums[:mid]) + sorted(nums[mid:])
        
        le = 0
        ri = mid
        
        while le < mid and ri < len(nums):
            while le < mid and nums[le] <= nums[ri]<<1:
                le += 1
            count += mid - le
            ri += 1
        
        return count