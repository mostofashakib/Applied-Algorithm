"""
LeetCode Problem: 35. Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity : O(log(N))
Space complexity : O(1).
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low+high)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        # if i reach here that means the target is not present in the nums array hence return the position of low
        return low