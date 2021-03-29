"""
LeetCode Problem: 994. Rotting Oranges
Link: https://leetcode.com/problems/rotting-oranges/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        rottenOrange = deque()
        freshOrange = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # Preprocess to find rotten and fresh oranges
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    rottenOrange.append((r, c, 0))
                elif grid[r][c] == 1:
                    freshOrange.add((r, c))
                    
        timeStamps = 0
        
        while rottenOrange:
            x, y, timeStamps = rottenOrange.popleft()
            
            for dx, dy in directions:
                newX = x + dx
                newY = y + dy
                
                if 0 <= newX < rows and 0 <= newY < columns and (newX, newY) in freshOrange:
                    freshOrange.remove((newX, newY))
                    rottenOrange.append((newX, newY, timeStamps + 1))
            
        return timeStamps if not freshOrange else -1