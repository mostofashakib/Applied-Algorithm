"""
LeetCode Problem: 263. Ugly Number
Link: https://leetcode.com/problems/ugly-number/
Language: Python
Written by: Mostofa Adib Shakib

Time Compplexity: O(long n)
Space Complexity: O(1)
"""

class Solution:
    def isUgly(self, num: int) -> bool:
        # Edge case
        if num == 1:
            return True
        
        # A helper function that checks if a given number is a multiple of 2, 3 or 5
        def isMultiple(num):
            # we keep dividing as long as num is greater than 1 and is not a float
            while num > 1 and num % 1 == 0:
                if num % 2 == 0:
                    num = num//2
                elif num % 3 == 0:
                    num = num//3
                elif num % 5 == 0:
                    num = num // 5
                else:
                    break
                
            return True if num == 1 else False
        
        # return true if num is a multiple or return False
        if isMultiple(num):
            return True
        else:
            return False