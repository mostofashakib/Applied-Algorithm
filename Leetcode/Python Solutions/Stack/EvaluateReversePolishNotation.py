"""
LeetCode Problem: 150. Evaluate Reverse Polish Notation
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # A helper function to check if a given char is an operator or not
        def isOperators(char):
            if char == '+' or char == '-' or char == '*' or char == '/':
                return True
            else:
                return False
            
        stack = []      # Initializes a stack
        
        # Traverses through the token array
        for char in tokens:
            # If char is not an operator then push it to the stack
            if isOperators(char) == False:
                stack.append( int(char) )
            # If the char is an operator that carry out operations
            else:
                firstNumber = stack.pop()       # Pops off the top-most element from the stack
                secondNumber = stack.pop()      # Pops off the second top-most element from the stack
                
                # carries out a mathematical operation depending on the operator
                if char == '+':
                    stack.append(secondNumber+firstNumber)
                elif char == '-':
                    stack.append(secondNumber-firstNumber)
                elif char == '*':
                    stack.append(secondNumber*firstNumber)
                else:
                    stack.append( int(secondNumber/firstNumber) )   # We cast int in order to truncate decimals
                    
        return stack[-1]