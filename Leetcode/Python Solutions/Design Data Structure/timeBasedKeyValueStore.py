"""
LeetCode Problem: 981. Time Based Key-Value Store
Link: https://leetcode.com/problems/time-based-key-value-store/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(logN)
Space Complexity: O(N)
"""

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.hashMap[key], (-timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        maxHeap = self.hashMap[key]
        
        for time, value in maxHeap:
            if -time <= timestamp:
                return value
                
        return ""