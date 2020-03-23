"""
LeetCode Problem: 33. Search in Rotated Sorted Array
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Language: Python
Written by: Mostofa Adib Shakib

Algorithm:

1) Initiate start to be equal to 0, and end to be equal to n - 1.

2) Perform standard binary search. While start <= end:
    Take an index in the middle mid as a pivot.

    If nums[mid] == target, the job is done, return mid.

    Now there could be two situations:

        Pivot element is larger than the first element in the array, i.e. the part of array from the first element to the pivot one is non-rotated.

            If the target is in that non-rotated part as well: go left: end = mid - 1.

            Otherwise: go right: start = mid + 1.

        Pivot element is smaller than the first element of the array, i.e. the rotation index is somewhere between 0 and mid. That means that the part of array from the pivot element to the last one is non-rotated.

            If target is in that non-rotated part as well: go right: end = mid + 1.

            Otherwise: go left: start = mid - 1.

3) We're here because the target is not found. Return -1.

Time complexity : O(log(N))
Space complexity : O(1).
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[start]:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target and nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1