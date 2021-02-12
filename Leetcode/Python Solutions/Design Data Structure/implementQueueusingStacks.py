"""
LeetCode Problem: 232. Implement Queue using Stacks
Link: https://leetcode.com/problems/implement-queue-using-stacks/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: Amortized O(1)
Space Complexity: O(n)
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        if not self.stack2:
            self.stack2.append(x)
        else:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            
            self.stack1.append(x)
            
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        if len(self.stack2) == 0:
            return True
        return False
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()