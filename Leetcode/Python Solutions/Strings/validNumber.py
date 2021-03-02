"""
LeetCode Problem: 65. Valid Number
Link: https://leetcode.com/problems/valid-number/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        i = 0
        length = len(s)
        countNums = 0
        countEs = 0
        countDecimals = 0
        
        # Consume all the write spaces at the beginning of the string
        while i< length and s[i] == ' ':
            i += 1
        
        # Consume the sign character if at the start of the string
        if i < length and (s[i] == '+' or s[i] == '-'):
            i += 1
        
        # Count all the deciamls and integer before the exponent character
        while i < length and ( (s[i] >= '0' and s[i] <= '9') or s[i] == '.' ):
            if s[i] == '.':
                countDecimals += 1
            else:
                countNums += 1
            i += 1
        
        # Return False if there is more than one decimal or if the integer count is 0
        if countDecimals > 1 or countNums == 0:
            return False
        
        # Consume the exponent if present in the given string
        if i < length and ( s[i] == 'e' or s[i] == 'E' ):
            i += 1
            
            # Consume the sign character if present
            if i < length and (s[i] == '+' or s[i] == '-'):
                i += 1
            
            # Count the number of integers present after the exponent
            while i < length and (s[i] >= '0' and s[i] <= '9'):
                i += 1
                countEs += 1
            
            # Return false if the number of integers in the exponent part is 0
            if countEs == 0:
                return False
        
        # Consume all the white spaces at the end of the string
        while i < length and s[i] == ' ':
            i += 1
        
        # This will only return true if the string is a valid number with the given constraints
        return i == length