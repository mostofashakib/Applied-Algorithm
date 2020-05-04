"""
LeetCode Problem: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Language: Python
Written by: Mostofa Adib Shakib

Time Compplexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(': ')', '{':'}', '[':']'}
        stack = []
        
        for i in s:
            if i in hashmap:
                stack.append(i)
                
            elif len(stack) > 0 and i == hashmap[stack[-1]]:
                stack.pop()
                
            else:
                return False
                
        return stack == []