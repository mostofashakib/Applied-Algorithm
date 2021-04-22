"""
LeetCode Problem: 346. Moving Average from Data Stream
Link: https://leetcode.com/problems/moving-average-from-data-stream/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(1)
Space Complexity: O(N)
"""

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.amount = 0
        self.capacity = size
        self.count = 0

    def next(self, val: int) -> float:
        if self.count < self.capacity:
            self.queue.append(val)
            self.amount += val
            self.count += 1
            
            return self.amount / self.count 
        else:
            self.amount -= self.queue.pop(0)
            self.amount += val
            self.queue.append(val)
            
            return self.amount / self.capacity