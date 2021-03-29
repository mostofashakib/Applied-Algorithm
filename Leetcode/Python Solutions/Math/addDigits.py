"""
LeetCode Problem: 258. Add Digits
Link: https://leetcode.com/problems/add-digits/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(1)
Space Complexity: O(1)

Digital Roots:

    If n = 0
        dr(n)=0

    If n = 9K:
        dr(n) = 9
    ​   
    If n != 9K:
        dr(n) = n % 9
"""

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
                
        if num % 9 == 0:
            return 9
        
        return num % 9