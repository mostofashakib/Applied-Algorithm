"""
LeetCode Problem: 227. Basic Calculator II
Link: https://leetcode.com/problems/basic-calculator-ii/
Language: Python
Written by: Mostofa Adib Shakib

Algorithm:

Calculate the magnitude of all the values seen in the string and find their sum

Time Complexity: O(N)
Space Complexity: O(N)
"""


# with Stack


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'      # previous operator
        num = 0         # checks for numbers with more than 2 digits 
        s += '+'
        
        for i in s:
            if i.isdigit():          # checks if a given character is a digit
                num = num * 10 + int(i)
            elif i == ' ':           # skip if whitespace
                continue
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    res = stack.pop()
                    stack.append(res*num)
                elif sign == '/':
                    res = stack.pop()
                    stack.append(int(res/num))     # ensures ceiling value regardless of the number being positive or negative.
                num = 0                            # resets the number tracker when we see an operator.
                sign = i                           # sets the operator for the next number
                
        return sum(stack)                          # sums up all the magnitude of the values



# Without stack

class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        temp = 0                    # used instead of stack
        num = 0
        curr = "+"
        
        for elem in s + "+":
            if elem in "*/-+":
                if curr == "+":
                    result += temp
                    temp = num
                elif curr == "-":
                    result += temp
                    temp = -num
                elif curr == "*":
                    temp *= num
                elif curr == "/":
                    temp = int(temp/num)
                curr = elem
                num = 0
            else:
                if elem.isdigit():
                    num = num*10 + int(elem)
        
        return result + temp