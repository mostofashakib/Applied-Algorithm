"""
LeetCode Problem: 856. Score of Parentheses
Link: https://leetcode.com/problems/score-of-parentheses/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Optimal Solution
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def scoreOfParentheses(self, S):
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 1 << bal
        return ans


# Stack based Solution
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        length = len(S)
        
        for i in range(length):
            char = S[i]
            
            if char == "(":
                stack.append(char)
            
            elif stack and stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                num = 0
                while stack and stack[-1] != '(':
                    num += stack.pop()
                stack.pop()
                stack.append(2*num)
        
        return sum(stack)