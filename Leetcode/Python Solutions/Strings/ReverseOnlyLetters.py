"""
LeetCode Problem: 917. Reverse Only Letters
Link: https://leetcode.com/problems/reverse-only-letters/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

import string

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        low = 0
        high = len(S) - 1
        S = list(S)                       # converts the string to a char array
        correct  = string.ascii_letters   # contains all characters from A-Z & a-z
        
        while low < high:
            if S[low] not in correct:
                low += 1
            elif S[high] not in correct:
                high -= 1
            else:
                S[low], S[high] = S[high], S[low]
                low += 1
                high -= 1
                
        return ''.join(S)