"""
LeetCode Problem: 201. Bitwise AND of Numbers Range
Link: https://leetcode.com/problems/bitwise-and-of-numbers-range/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(1)
Space Complexity: O(1)
"""

"""
Bit Shift
Time Complexity: O(1)
Space Complexity: O(1)

Explanation:
The idea is that we shift both numbers to the right, until the numbers become equal, i.e. the numbers are reduced into their common prefix.
Then we append zeros to the common prefix in order to obtain the desired result, by shifting the common prefix to the left.
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0   
        # find the common 1-bits[common prefix]
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift

"""
Brian Kernighan's Algorithm
Time Complexity: O(1)
Space Complexity: O(1)

Explanation:
When we do AND bit operation between number and number-1, the rightmost bit of one in the original number would be turned off (from one to zero).
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # turn off rightmost 1-bit after the common prefix
            n = n & (n - 1)
        return m & n


# Bruteforce Not a good solutions

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if (n-m) == 0: return m
        if m > 2000000 and (n-m) == 1: return m
        if m == 0 or n > 2000000: return 0
        flag = False
        ans = 0
        for i in range(m+1, n+1):
            if flag != True:
                ans = (i-1) & i
                flag = True
            else:
                ans = ans & i
        return ans