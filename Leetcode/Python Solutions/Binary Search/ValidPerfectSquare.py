"""
LeetCode Problem 367. Valid Perfect Square
Link: https://leetcode.com/problems/valid-perfect-square/
Written by: Mostofa Adib Shakib
Language: Python

Observation:

1) Number less than 2 will always form perfect squares so return True.
2) The number will always be in the first half of the array. Hence, we can discard the second half.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num <= 1: return True
        
        left = 2
        right = num//2
        
        while left <= right:
            
            mid = (left + right) // 2
            
            guess = mid * mid
            
            if guess == num:
                return True
            
            elif guess < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False