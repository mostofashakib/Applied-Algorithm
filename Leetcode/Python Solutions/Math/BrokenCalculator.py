"""
LeetCode Problem: 991. Broken Calculator
Link: https://leetcode.com/problems/broken-calculator/
Language: Python
Written by: Mostofa Adib Shakib

Two operations:
    => Double: Multiply the number on the display by 2
    => Decrement: Subtract 1 from the number on the display

Time Complexity: O(n)
Space Complexity: O(1)
"""

from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def brokenCalc(self, X: int, Y: int) -> int:
        if(X == Y): 
            return 0

        if(X > Y): 
            return X - Y 

        if Y % 2 == 0:
            return 1 + self.brokenCalc(X, Y // 2) 

        else: 
            return 1 + self.brokenCalc(X, Y + 1)