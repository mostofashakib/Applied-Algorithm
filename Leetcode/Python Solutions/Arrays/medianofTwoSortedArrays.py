"""
LeetCode Problem 4. Median of Two Sorted Arrays
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(log(min(m,n))
Space Complexity: O(1)
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n = len(nums1)
        m = len(nums2)
        
        low = 0
        high = n
                
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n) // 2 - partitionX
                        
            maxLeftX = nums1[partitionX-1] if partitionX != 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX != n else float('inf')
            
            maxLeftY = nums2[partitionY-1] if partitionY != 0 else float('-inf')
            minRightY = nums2[partitionY] if partitionY != m else float('inf')
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (n+m) % 2 == 0:
                    maximum = max(maxLeftX, maxLeftY)
                    minimum = min(minRightX, minRightY)
                    return (maximum + minimum) / 2.0
                else:
                    return min(minRightX, minRightY)
            
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1