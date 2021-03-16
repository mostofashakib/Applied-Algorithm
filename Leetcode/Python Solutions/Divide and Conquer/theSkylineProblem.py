"""
LeetCode Problem: 218. The Skyline Problem
Link: https://leetcode.com/problems/the-skyline-problem/
Further Reading: https://briangordon.github.io/2014/08/the-skyline-problem.html
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildingPositions = []
        
        for x, y, h in buildings:
            buildingPositions.append((x, -h, y))
            buildingPositions.append((y, 0, 0))
        
        maxHeap = []
        ans = []
        buildingPositions = sorted(buildingPositions)
        
        for x, h, y in buildingPositions:
            while maxHeap and maxHeap[0][1] <= x:
                heappop(maxHeap)
            
            heappush(maxHeap, (h, y))
            curMax = -maxHeap[0][0]
            
            if not ans or ans[-1][1] != curMax:
                ans.append([x, curMax])
                
        return ans