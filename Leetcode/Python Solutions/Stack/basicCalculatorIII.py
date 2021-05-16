"""
LeetCode Problem: 227. Basic Calculator III
Link: https://leetcode.com/problems/basic-calculator-iii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

# Recursion + Stack

class Solution:
    def equationSolver(self, array):
        if not array:
            return 0
        
        stack = []
        num = 0
        curr = "+"
        
        while array:
            char = array.popleft()
            
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "(":
                num = self.equationSolver(array)
            else:
                if curr == "+":
                    stack.append(num)
                elif curr == "-":
                    stack.append(-num)
                elif curr == "*":
                    stack[-1] = stack[-1] * num
                elif curr == "/":
                    stack[-1] = int(stack[-1] / num)
                
                if char == ")":
                    break
                    
                curr = char
                num = 0
                
        return sum(stack)
    
    def calculate(self, s: str) -> int:
        s += "+"
        array = deque(list(s))
        return self.equationSolver(array)

# BNF Grammar

class Solution:
    # Standard parser implementation based on this BNF
    #   s := expression
    #   expression := term | term { [+,-] term] }
    #   term := factor | factor { [*,/] factor] }
    #   factor :== digit | '(' expression ')'
    #   digit := [0..9]
    
    def expTree(self, s: str) -> 'Node':
        tokens = collections.deque(list(s))
        return self.parse_expression(tokens)

    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)
        while len(tokens) > 0 and tokens[0] in ['+', '-']:
            op = tokens.popleft()
            rhs = self.parse_term(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs
    
    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)
        while len(tokens) > 0 and tokens[0] in ['*', '/']:
            op = tokens.popleft()
            rhs = self.parse_factor(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    def parse_factor(self, tokens):
        if tokens[0] == '(':
            tokens.popleft() # consume '('
            node = self.parse_expression(tokens)
            tokens.popleft() # consume ')'
            return node
        else:
            # Single operand
            token = tokens.popleft()
            return Node(val=token)