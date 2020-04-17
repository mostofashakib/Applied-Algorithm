"""
LeetCode Problem: 200. Number of Islands
Link: https://leetcode.com/problems/number-of-islands/
Language: Python
Written by: Mostofa Adib Shakib


Number of rows = M
Number of columns = N
Time complexity : O(M×N)
Space complexity : O(M×N)
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DepthFirstSearch(row, col, grid):
            # out of bound or encountered a cell with 0
            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) -1 or grid[row][col] == '0':
                return 0
            if grid[row][col] == '1':
                grid[row][col] = '0'   # change the cell to visited
                DepthFirstSearch(row, col-1, grid)
                DepthFirstSearch(row, col+1, grid)
                DepthFirstSearch(row-1, col, grid)
                DepthFirstSearch(row+1, col, grid)
                
            return 1                   # one island
            
        maximumIslands = 0             # maximum number of islands
        
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    maximumIslands +=  DepthFirstSearch(row,column,grid)
        return maximumIslands