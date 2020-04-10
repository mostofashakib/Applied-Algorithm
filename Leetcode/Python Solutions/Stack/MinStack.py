"""
LeetCode Problem: 155. Min Stack
Link: https://leetcode.com/problems/min-stack/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(1)
Space Complexity: O(N)
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        self.minStack = []

    def push(self, x: int) -> None:
        
        if len(self.minStack) == 0:
            self.minStack.append(x)
        elif x <= (self.minStack[-1]):
            self.minStack.append(x)
            
        self.array.append(x)
        
    def pop(self) -> None:
        temp = self.array.pop()
        
        if temp == self.minStack[-1]:
            self.minStack.pop()
        
        
    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()