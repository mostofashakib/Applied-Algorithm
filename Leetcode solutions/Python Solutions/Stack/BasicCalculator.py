"""
LeetCode Problem: 227. Basic Calculator II
Link: https://leetcode.com/problems/basic-calculator-ii/
Language: Python
Written by: Mostofa Adib Shakib

Algorithm:
    1) Iterate the expression string one character at a time. Since we are reading the expression character by character, we need to be careful when we are reading digits and non-digits.
    2) The operands could be formed by multiple characters. A string "123" would mean a numeric 123, which could be formed as: 123 >> 120 + 3 >> 100 + 20 + 3.
Thus, if the character read is a digit we need to form the operand by multiplying 10 to the previously formed continuing operand and adding the digit to it.
    3) Whenever we encounter an operator such as + or - we first evaluate the expression to the left and then save this sign for the next evaluation.
    4) If the character is an opening parenthesis (, we just push the result calculated so far and the sign on to the stack (the sign and the magnitude)
and start a fresh as if we are calculating a new expression.
    5) If the character is a closing parenthesis ), we first calculate the expression to the left.
The result from this would be the result of the expression within the set of parenthesis that just concluded.
This result is then multiplied with the sign, if there is any on top of the stack.
Remember we saved the sign on top of the stack when we had encountered an open parenthesis?
This sign is associated with the parenthesis that started then, thus when the expression ends or concludes, we pop the sign and multiply it with result of the expression.
It is then just added to the next element on top of the stack.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand
