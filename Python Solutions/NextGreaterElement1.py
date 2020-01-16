"""
LeetCode Problem: 496. Next Greater Element I
Link: https://leetcode.com/problems/next-greater-element-i/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # Handling edge cases

        if not nums1:
            return []
        if not nums2:
            return [-1]*len(nums1)
        
        ans = []
        
        for i in nums1:
            j = nums2.index(i)
    
            if j < len(nums2) -1:
                for k in range(j+1, len(nums2)):
                    if nums2[k] > i:
                        ans.append(nums2[k])
                        break
                else:
                    ans.append(-1)
            else:
                ans.append(-1)
        return ans