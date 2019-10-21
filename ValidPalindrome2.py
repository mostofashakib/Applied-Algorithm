"""
680 Leetcode. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/
"""

"""

This program uses two pointers one that starts from the beginning of the string and the other starts from the end of the string. If the 
first character of the string is equal to the last character of the string then we increment the start pointer and decrement the last pointer.
If we reach the midpoint of the array and the first half is equal to the last half then we return True. If we have a disagreement then we use a
helper method. The helper method takes two versions of the substring from were the disagreement starts to see if anyone of those versions are palindromes themselves if either of them
is a palindrome then the program returns True otherwise the helper method returns False.

"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(s, i, j):
            i = i
            j = j 
        
            while i < j:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True
        
        if s == s[::-1]: return True
        
        i = 0
        j = len(s) -1 
        
        while i < j:
            if s[i] != s[j]:
                return helper(s, i+1, j) or helper(s, i, j-1)
            else:
                i += 1
                j -= 1
        return True