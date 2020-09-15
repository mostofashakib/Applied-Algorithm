"""
LeetCode Problem: 64. Minimum path sum
Link: https://leetcode.com/problems/minimum-path-sum/
Written by: Mostofa Adib Shakib
Language: Python
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        rowLength = len(grid)
        columnLength = len(grid[0])
        
        for row in range(rowLength):
            for column in range(columnLength):
                if row == 0 and column == 0:
                    continue
                elif row == 0:
                    grid[row][column] += grid[row][column-1]
                elif column == 0:
                    grid[row][column] += grid[row-1][column]
                else:
                    grid[row][column] += min(grid[row][column-1], grid[row-1][column])
                
        return grid[-1][-1]