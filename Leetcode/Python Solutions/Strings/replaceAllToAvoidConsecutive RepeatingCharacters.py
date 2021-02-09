"""
LeetCode Problem: 1576. Replace All ?'s to Avoid Consecutive Repeating Characters
Link: https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def modifyString(self, s: str) -> str:
        length = len(s)
        lowerCaseLetter = string.ascii_lowercase
        
        # Edge case
        if length == 1:
            return 'a' if s == '?' else s
        
        # If the given string starts with ?
        if s[0] == '?':
            for character in lowerCaseLetter:
                if s[1] != character:
                    s = character + s[1:]
                    break
        
        # If the given string ends with ?
        if s[-1] == '?':
            for character in lowerCaseLetter:
                if s[-2] != character:
                    s = s[:-1] + character
                    break
        
        # Takes care of all other ? in the string
        for i in range(1, length-1):
            if s[i] == '?':
                # Try all possible characters
                for character in lowerCaseLetter:
                    if s[i-1] != character and s[i+1] != character:
                        s = s[:i] + character + s[i+1:]
                        break
        return s