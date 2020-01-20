"""
LeetCode Problem: 231. Power of Two
Link: https://leetcode.com/problems/power-of-two/
Language: Python
Written by: Mostofa Adib Shakib

Algorithm:

Power of two has just one 1-bit.

x & (x - 1) sets this 1-bit to zero, and hence one has to verify if the result is zero x & (x - 1) == 0.

Time complexity :  O(1).
Space complexity : O(1).
"""

class Solution:
    def isPowerOfTwo(self, x: int) -> bool:
        return False if x == 0 else (x & x-1) == 0