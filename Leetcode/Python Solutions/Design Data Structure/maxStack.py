"""
LeetCode Problem: 716. Max Stack
Link: https://leetcode.com/problems/max-stack/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            maximum = max(self.stack[-1][1], x)
            self.stack.append((x, maximum))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        maximum = self.stack[-1][1]
        aux = []
        
        while self.stack[-1][0] != maximum:
            aux.append(self.stack.pop()[0])
        
        self.stack.pop()
        
        while aux:
            self.push(aux.pop())

        return maximum