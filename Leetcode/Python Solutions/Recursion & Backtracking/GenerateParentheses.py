"""
LeetCode Problem: 22. Generate Parentheses
Link: https://leetcode.com/problems/generate-parentheses/submissions/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity: Bounded by a catalan number
"""

"""
Conditions that makes parenthesis balanced:
1) An empty string is a string in which parenthesis are balanced.
2) The addition of a leading left parenthesis and a trailing right parenthesis to a string in which parenthesis are matched.
3) The concatenation of two strings in which parenthesis are balanced results in a new string where the parenthesis are also balanced.

Constraits:
1) The number of opening parenthesis should be less than the twice the maximum of pair required(Condition 1)
2) The number of closing parenthesis should be less than the number of opening parenthesis(Condition 2)
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def backtrack(array, current_string, NoleftParenthesis, NoRightParenthesis, maximumLength):
            if len(current_string) == maximumLength *2:    # if have found one of the solutions
                array.append(current_string)
                return
            if NoleftParenthesis < maximumLength:        # we can place an opening parenthesis
                backtrack(array, current_string + '(', NoleftParenthesis+1, NoRightParenthesis, maximumLength)
            if NoRightParenthesis < NoleftParenthesis:   # we can place a closing parenthesis
                backtrack(array, current_string + ')', NoleftParenthesis, NoRightParenthesis+1, maximumLength)
        
        array = []                           # the array containing all the solutions
        backtrack(array, "", 0, 0, n)        # calling the helper method
        return array                         # returns the answer array at the end