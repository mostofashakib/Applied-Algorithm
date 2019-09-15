"""
LeetCode Problem: 896. Monotonic Array
Link: https://leetcode.com/problems/monotonic-array/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 0: return False
        if len(A) == 1: return True
        
        is_monotonic_asc = is_monotonic_desc = True
        
        for i in range(1,len(A)):
            if A[i] < A[i - 1]:
                is_monotonic_asc = False
            if A[i] > A[i - 1]:
                is_monotonic_desc = False
                
        return is_monotonic_asc or is_monotonic_desc