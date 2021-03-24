"""
LeetCode Problem: 1249. Minimum Remove to Make Valid Parentheses
Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        
        for index, char in enumerate(s):
            if char not in "()":
                continue
            elif char == "(":
                stack.append(index)            
            elif char == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    s[index] = ''
        
        # If there are excessive opening parentheses      
        while len(stack) > 0:
            s[stack.pop()] = ''
            
        return "".join(s)