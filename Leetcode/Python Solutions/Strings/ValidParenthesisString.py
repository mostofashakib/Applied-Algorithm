"""
LeetCode Problem: 678. Valid Parenthesis String
Link: https://leetcode.com/problems/valid-parenthesis-string/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
    Let diff be count of left parenthesis minus count of right parenthesis.

    When we meet:

    '(' = we increment diff.
    ')' = we decrement diff.
    '*' = we have three choices which makes the diff become a range [diff - 1, diff + 1].

    So we use maxDiff/minDiff to record the maximum/minimum diff we can get.

    When we meet:

    (, ++maxDiff and ++minDiff.
    ), --maxDiff and --minDiff.
    *, ++maxDiff and --minDiff.

    If maxDiff become negative, it means it's already invalid, we should return false.

    Whenever minDiff falls below 0, we should force it to be 0 because we never accept negative diff during the process.

    After scanning through string s, as long as minDiff is 0, this string can be a valid one.

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        # special cases
        
        if not s: return True                                # An empty string is a valid string
        if s[0] == ')': return False                         # No way this string is going to be valid
        
        minOpenParenthesis = 0
        maxOpenParenthesis = 0
        
        for i in s:
            if i == '(':
                minOpenParenthesis += 1
                maxOpenParenthesis += 1
            elif i == ')':
                minOpenParenthesis -= 1
                maxOpenParenthesis -= 1
            else:
                minOpenParenthesis -= 1
                maxOpenParenthesis += 1
                
            if maxOpenParenthesis < 0:
                return False
            
            minOpenParenthesis = max(minOpenParenthesis, 0)  # Force min so that it nevers goes below 0
            
        return minOpenParenthesis == 0