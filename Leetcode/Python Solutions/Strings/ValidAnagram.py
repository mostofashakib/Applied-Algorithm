"""
LeetCode Problem: 242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Written by: Mostofa Adib Shakib
Language: Python
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        length1 = len(s)
        length2 = len(t)
        
        if length1 != length2:
            return False
        
        s = sorted(s)   #sorted the string in alphanumeric order
        t = sorted(t)   #sorted the string in alphanumeric order
        
        for i in range(0, length1):
            if s[i] != t[i]:
                return False    # return false if the two sorted strings are not the same.

        return True     # if the sorted strings are same return True