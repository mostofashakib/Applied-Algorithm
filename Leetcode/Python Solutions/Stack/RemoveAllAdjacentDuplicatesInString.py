"""
LeetCode Problem: 1047. Remove All Adjacent Duplicates In String
Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Language: Python
Written by: Mostofa Adib Shakib

Time Compplexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []          # Initialize a stack
        
        # If the stack is not empty and the top of the stack is equal to char. Pop the element from the stack
        # else append the char to the stack
        
        for char in S:
            if stack and stack[-1] == char:
                stack.pop()
            # 
            else:
                stack.append(char)
        
        return ''.join(stack)   # create a string from the characters of the stack