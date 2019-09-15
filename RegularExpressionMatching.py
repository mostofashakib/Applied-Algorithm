"""
LeetCode Problem: 10. Regular Expression Matching
Link: https://leetcode.com/problems/regular-expression-matching/
Language: Python
Written by: Mostofa Adib Shakib
"""

import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return s in re.findall(p, s)