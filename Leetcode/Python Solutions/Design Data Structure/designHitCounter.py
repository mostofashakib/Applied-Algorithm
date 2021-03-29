"""
LeetCode Problem: 362. Design Hit Counter
Link: https://leetcode.com/problems/design-hit-counter/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity:
    Hit: O(1)
    getHits:
        Average Case: O(1)
        Worst Case: O(N)
Space Complexity: O(N)
"""

class HitCounter:
    def __init__(self):
        self.data = deque()

    def hit(self, timestamp: int) -> None:
        self.data.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # while len(self.data) and timestamp - self.data[0] >= 300:
        #     self.data.popleft()
        
        while len(self.data) and timestamp - self.data[0] >= 300:
            self.data.popleft()
            
        return len(self.data)