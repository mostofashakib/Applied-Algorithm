"""
LeetCode Problem: 316. Remove Duplicate Letters
Link: https://leetcode.com/problems/remove-duplicate-letters/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        #purpose: to have as less characters as possible to return the characters subset lexicographically
        stack = []
        
        #purpose: to record if the character is seen earlier or not
        seen = set()
        
        #purpose: to record last index of each character
        last_occurrence = {}
        
        for i in range(len(s)):
            last_occurrence[s[i]] = i
            
        for index, character in enumerate(s):
            
            if character not in seen:
                
                #   if current character is not seen earleir:
                #   while the stack is not empty:
                #       a)compare current character with previous character on stack.
                #       b) if lexicographically less and the previous character has future occurences, pop the previous character from stack.
                #       c) delete the previous character from seen dict
                #
                #   add current character to seen
                #   append current character to stack
                #   return contents of stack as result
                while stack and character < stack[-1] and index < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(character)
                stack.append(character)
        
        return ''.join(stack)