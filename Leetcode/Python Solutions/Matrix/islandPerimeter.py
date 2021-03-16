"""
LeetCode Problem: 463. Island Perimeter
Link: https://leetcode.com/problems/island-perimeter/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n*m)
Space Complexity: O(1)
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        perimeter = 0
        rows = len(grid)
        columns = len(grid[0])
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    perimeter += 4                      # Check for best possible scenario
                    
                    # If anyone of these conditions are true then either the top or the left cell is a land
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                        
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
        
        return perimeter