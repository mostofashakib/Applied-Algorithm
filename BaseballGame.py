"""

LeetCode Problem: 682. Baseball Game
Link: https://leetcode.com/problems/baseball-game/
Language: Python
Written by: Mostofa Adib Shakib

"""

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        length = len(ops)
        stack = []
        index = 0
        
        while(length>0):
            if ops[index] == '+':
                stack.append(stack[-1] + stack[-2])
            elif ops[index] == 'C':
                stack.pop()
            elif ops[index] == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(ops[index]))
            index += 1
            length -= 1
        return sum(stack) 