"""
LeetCode Problem 1416. Restore The Array

Link: https://leetcode.com/problems/restore-the-array/
Written by: Mostofa Adib Shakib
Language: Python
        
For each position in the string we go at most t steps backward. If a number is possible which does not start with 0 and lies
between 1 and k, we add that to our current count.

Time : O(length of the given string * max number of digits k can have) = O(length of the given string * 10)
Space : O(length of the given string)
"""

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        length = len(s)
        backWardTurns = len(str(k))
        largePrimeNumber = 1000000007
        dp = [0] * (length+1)
        dp[0] = 1
        dp[1] = 1
        
        for index in range(1, length):
            for steps in range(backWardTurns):
                if index-steps >= 0 and  1 <= int(s[index-steps:index+1]) <= k and s[index-steps:index+1][0] != "0":
                    dp[index+1] += dp[index-steps]
        
        return dp[-1] % largePrimeNumber