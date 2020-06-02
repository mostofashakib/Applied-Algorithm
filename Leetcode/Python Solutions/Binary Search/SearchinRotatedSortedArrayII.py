"""
LeetCode Problem: 81. Search in Rotated Sorted Array II
Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(log(N))
Space Complexity: O(1)

"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return True
            
            elif nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
        return False