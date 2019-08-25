"""
LeetCode Problem: 266. Palindrome Permutation
Link: https://leetcode.com/articles/palindrome-permutation/
Language: Python
Written by: Mostofa Adib Shakib

"""

class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        unpaired_chars = set()
        
        for char in s:
            if char not in unpaired_chars:
                unpaired_chars.add(char)
            else:
                unpaired_chars.remove(char)
                
        return len(unpaired_chars) <= 1