"""
LeetCode Problem: 151. Reverse words in a string
Link: https://leetcode.com/problems/reverse-words-in-a-string/
Written by: Mostofa Adib Shakib
Language: Python

"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        final = s.strip().split()
        final.reverse()
        
        return ' '.join(final)
        