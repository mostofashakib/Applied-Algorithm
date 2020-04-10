"""
Leetcode 844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        arr = list(S)
        arr1 = list(T)
        length = len(arr)
        length1 = len(arr1)
        i = 1
        j = 1
        
        while i < length:
            if arr[0] == '#':
                arr.pop(0)
                length -= 1
                i = 0
                
            elif arr[i] == '#':
                arr.pop(i)
                arr.pop(i-1)
                length -= 2
                i = 0
            i += 1
            
        while j < length1:
            if arr1[0] == '#':
                arr1.pop(0)
                length1 -= 1
                j = 0
                
            elif arr1[j] == '#':
                arr1.pop(j)
                arr1.pop(j-1)
                length1 -= 2
                j = 0
                
            j += 1
            
        return arr == arr1