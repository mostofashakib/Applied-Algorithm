"""
LeetCode Problem: 301. Remove Invalid Parentheses
Link: https://leetcode.com/problems/remove-invalid-parentheses/
Language: Python
Written by: Mostofa Adib Shakib
"""

from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        found = False   # boolean flag to indicate a valid parenthesis has been found
        dist = set()    # a set to make all the parenthesis distinct
        result = []     # keeps all the combinations of unique valid parenthesis
        queue = deque([s])   # a deque is initialized
        
        while queue:
            paren = queue.popleft()
            
            if self.isValid(paren) == True:  #checks if a given string is valid
                found = True
                result.append(paren)
            
            if found == False:
                for i in range(len(paren)):
                    if paren[i] in '()':     # if the traversed character is a bracket
                        paren_n = paren[:i] + paren[i+1:]  # skipping one bracket in a given string at a time
                        if paren_n not in dist:   # check is the paren_n is unique
                            dist.add(paren_n)     # adds the new unique string to the set
                            queue.append(paren_n) # adds the new unique string to the queue
                            
        return result    # returns the result array containing all the valid parentheses.
                    
    def isValid(self, string):
        if string == "": return True   # if the string is empty return True           
        balanced = 0                   # counts the total number of unmatched parenthesis
        
        for i in string:
            if i == '(':
                balanced += 1
            elif i == ')':
                balanced -= 1
                if balanced < 0:  # unmatched right parenthesis
                    return False
        return balanced == 0