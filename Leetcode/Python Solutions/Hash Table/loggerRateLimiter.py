"""
LeetCode Problem: 359. Logger Rate Limiter
Link: https://leetcode.com/problems/logger-rate-limiter/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(1)
Space Complexity: O(n)
"""

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        
        if message not in self.hashmap:
            self.hashmap[message] = timestamp
            return True
        
        else:
            if timestamp >= self.hashmap[message] + 10:                
                self.hashmap[message] = timestamp
                return True
            else:
                return False
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)