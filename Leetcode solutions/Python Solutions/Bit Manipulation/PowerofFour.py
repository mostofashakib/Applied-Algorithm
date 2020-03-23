"""
LeetCode Problem: 342. Power of Four
Link: https://leetcode.com/problems/power-of-four/
Language: Python
Written by: Mostofa Adib Shakib
"""

"""
Approach 1:

A number n is a power of 4 if following conditions are met.
    There is only one bit set in the binary representation of n (or n is a power of 2)
    The bits don’t AND(&) any part of the pattern 0xAAAAAAAA

Time complexity :  O(1).
Space complexity : O(1).
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
            return (num != 0 and ((num & (num - 1)) == 0) and not(num & 0xAAAAAAAA))


# Approach 2
# Time complexity :  O(1).
# Space complexity : O(1).

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while True:
            if num == 0:
                return False
            elif num== 1:
                return True
            elif num % 4 == 0:
                num = num/4
            else:
                return False