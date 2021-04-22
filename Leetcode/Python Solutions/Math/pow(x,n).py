"""
LeetCode Problem 50. Pow(x, n)
Link: https://leetcode.com/problems/powx-n/
Written by: Mostofa Adib Shakib
Language: Python

Time complexity: O(logn)
Space complexity: O(logn)
"""

class Solution:
    def myPowHelper(self, x, n):
        if n == 0:
            return 1.0
        
        if n == 1:
            return x
        
        half = self.myPowHelper(x, n//2)
        
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
        
        
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        
        return self.myPowHelper(x, n)