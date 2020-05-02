"""
LeetCode Problem 278. First Bad Version

Link: https://leetcode.com/problems/first-bad-version/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(logn)
Space complexity: O(1)
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        last = n
        
        while first <= last:
            mid = (first+last)//2
            if isBadVersion(mid) == False:
                first = mid + 1
            elif isBadVersion(mid) == True:
                if isBadVersion(mid-1) == True:
                    last = mid - 1
                else:
                    return mid