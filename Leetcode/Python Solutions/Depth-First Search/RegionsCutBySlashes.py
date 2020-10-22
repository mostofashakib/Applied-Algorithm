"""
LeetCode Problem: 959. Regions Cut By Slashes
Link: https://leetcode.com/problems/regions-cut-by-slashes/
Video explanation: https://www.youtube.com/watch?v=aY5eXeJICss&t=1175s
Language: Python
Written by: Mostofa Adib Shakib

Number of rows = M
Number of columns = N
Time complexity : O(M×N)
Space complexity : O(M×N)
"""

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        def depthFirstSearch(row, column, typeCell, grid, visited):

            # Check to see if the cell is outside the boundary or was previously visited
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid) or visited[row][column][typeCell] == True:
                return
            
            # Mark the current cell visited
            visited[row][column][typeCell] = True
            
            # connect the adjacent cells

            if typeCell == 0:
                depthFirstSearch(row-1, column, 2, grid, visited)
                
            elif typeCell == 1:
                depthFirstSearch(row, column+1, 3, grid, visited)
                
            elif typeCell == 2:
                depthFirstSearch(row+1, column, 0, grid, visited)
            
            elif typeCell == 3:
                depthFirstSearch(row, column-1, 1, grid, visited)
            
            # connect the diagonal cells if there aren't any slashes
            # Alternate between diagonal cells
            if grid[row][column] != '\\':

                depthFirstSearch(row, column, typeCell ^ 3, grid, visited)
                
            if grid[row][column] != '/':
                depthFirstSearch(row, column, typeCell ^ 1, grid, visited)
        
        N = len(grid)
        
        visited = [ [ [False for i in range(4)] for j in range(N) ] for k in range(N) ]
                
        numberOfCuts = 0
        
        for row in range(N):
            for col in range(N):
                for typeCell in range(4):
                    # if the cell is not visited
                    if visited[row][col][typeCell] == False:
                        depthFirstSearch(row, col, typeCell, grid, visited)
                        numberOfCuts += 1
        
        return numberOfCuts