"""
LeetCode Problem: 1614. Maximum Nesting Depth of the Parentheses
Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        if not s or len(s) == 1 and s[0] != '(' and s[0] != ')':
            return 0
        
        length = len(s)
        balance = 0
        maximum = 0
        
        for i in range(length):
            character = s[i]
            
            if character == '(':
                balance += 1
                maximum = max(balance, maximum)
                
            elif character == ')':
                balance -= 1
                
        return maximum