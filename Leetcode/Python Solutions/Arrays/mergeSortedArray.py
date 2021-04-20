"""
LeetCode Problem: 88. Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N+M)
Space Complexity: O(1)
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:        
        if not nums2:
            return nums1
        
        p1 = m - 1
        p2 = n - 1
        
        for i in range(m+n-1, -1, -1):
            if p2 < 0:
                break
                
            elif p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1