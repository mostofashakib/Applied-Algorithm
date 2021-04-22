"""
LeetCode Problem: 778. Swim in Rising Water
Link: https://leetcode.com/problems/swim-in-rising-water/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^2logN)
Space Complexity: O(N^2)
"""

class Solution:
    def helperBFS(self, grid, height, numOfRows, numOfCols):
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque([(0, 0)])
        visited = set((0, 0))
        
        if grid[0][0] > height:
            return False
        
        while queue:
            r, c = queue.popleft()
            
            if r < 0 or c < 0 or r >= numOfRows or c >= numOfCols:
                continue
            
            if grid[r][c] == grid[-1][-1]:
                return True
            
            for direct in directions:
                directX = r + direct[0]
                directY = c + direct[1]
                
                if (directX, directY) not in visited and directX >= 0 and directY >= 0 and directX < numOfRows and directY < numOfCols:
                    if grid[directX][directY] <= height:
                        queue.append((directX, directY))
                        visited.add((directX, directY))
        return False  
      
      
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        numOfRows = len(grid)
        numOfCols = len(grid[0])
        
        low = 0
        high = numOfRows * numOfCols - 1
        result = float('inf')
        
        while low <= high:
            mid = (low+high)//2
            
            if self.helperBFS(grid, mid, numOfRows, numOfCols):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result