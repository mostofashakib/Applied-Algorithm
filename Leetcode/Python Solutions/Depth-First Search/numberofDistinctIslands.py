"""
LeetCode Problem: 694. Number of Distinct Islands
Link: https://leetcode.com/problems/number-of-distinct-islands/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)

X => Start
O => Out of bound or water
U => Up
L => Left
R => Right
D => Down
"""

class Solution:    
    def computePath(self, r, c, grid, rows, columns, direction):
        if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == 0:
            return "0"
        
        grid[r][c] = 0
        
        up = self.computePath(r+1, c, grid, rows, columns, "U")
        down = self.computePath(r-1, c, grid, rows, columns, "D")
        left = self.computePath(r, c-1, grid, rows, columns, "L")
        right = self.computePath(r, c+1, grid, rows, columns, "R")
        
        return direction + left + right + up + down
        
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    visited.add(self.computePath(r, c, grid, rows, columns, "X"))
                    
        return len(visited)