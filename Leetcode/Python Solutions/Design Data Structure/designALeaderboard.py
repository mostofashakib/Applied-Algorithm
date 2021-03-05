"""
LeetCode Problem: 1244. Design A Leaderboard
Link: https://leetcode.com/problems/design-a-leaderboard/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(nlogK)
Space Complexity: O(n)
"""

class Leaderboard:
    def __init__(self):
        self.hashMap = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.hashMap:
            self.hashMap[playerId] = score
        else:
            self.hashMap[playerId] += score
        
    def top(self, K: int) -> int:
        minHeap = []
                
        for x in self.hashMap.values():
            heappush(minHeap, x)
            
            if len(minHeap) > K:
                heappop(minHeap)
        
        return sum(minHeap)

    def reset(self, playerId: int) -> None:
        del self.hashMap[playerId]