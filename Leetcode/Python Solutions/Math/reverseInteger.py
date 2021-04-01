"""
LeetCode Problem: 7. Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def reverse(self, x: int) -> int:
        if -9 <= x <= 9:
            return x
        
        ans = 0
        flag = False
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        
        if x < 0:
            flag = True
            
        x = abs(x)
        
        while x > 0:
            lastDigit = x % 10
            ans = 10 * ans +  lastDigit
            x = x // 10
            
            if ans > INT_MAX or ans < INT_MIN:
                return 0
        
        return ans if flag == False else -ans