"""
LeetCode Problem: 344. Reverse String
Link: https://leetcode.com/problems/reverse-string/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s) - 1
        
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1