"""
LeetCode Problem: 326. Power of Three
Link: https://leetcode.com/problems/power-of-three/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Approach 1:
# Any integer number other than power of 3 which divides highest power of 3 value that integer can hold 3^19 = 1162261467 will give reminder non-zero.
# Time complexity :  O(1).
# Space complexity : O(1).

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        else:
            return 1162261467 % n == 0

# Approach 2
# Time complexity :  O(1)
# Space complexity : O(1)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while True:
            if n == 0:
                return False
            if n == 1:
                return True
            elif n%3 == 0: 
                n = n/3
            else:
                return False
