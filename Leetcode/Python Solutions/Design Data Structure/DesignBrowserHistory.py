"""
LeetCode Problem: 1472. Design Browser History
Link: https://leetcode.com/problems/design-browser-history/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)

Doubly Linked List:
    Move the current pointer according to the required operation
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        
    def visit(self, url: str) -> None:
        node = Node(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node
    
    def back(self, steps: int) -> str:
        while self.curr.prev != None and steps != 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
    
    def forward(self, steps: int) -> str:
        while self.curr.next != None and steps != 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)