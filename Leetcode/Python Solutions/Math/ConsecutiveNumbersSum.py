"""
LeetCode Problem 829. Consecutive Numbers Sum
Link: https://leetcode.com/problems/consecutive-numbers-sum/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n**0.5)
Space Complexity: O(1)
"""

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        upperLimit = ceil( (2*N + 0.25)**0.5 - 0.5) + 1
        
        
        for k in range(1, upperLimit):
            N -= k
            if N % k == 0:
                count += 1
        return count