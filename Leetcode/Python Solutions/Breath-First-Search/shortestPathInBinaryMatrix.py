"""
LeetCode Problem: 1091. Shortest Path in Binary Matrix
Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def isValid(self, grid, xRow, yCol, numRows, numCols):
        if xRow >= 0 and xRow < numRows and yCol >= 0 and yCol < numCols and grid[xRow][yCol] == 0:
            return True
        return False
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        
        if grid[0][0] == 1 or grid[-1][-1]:
            return -1
        
        queue = deque([(0, 0, 1)])
        directions = [(1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1), (0, 1), (0, -1)]
        targetCell = (numRows-1, numCols-1)
        visited = set((0, 0))
        
        while queue:
            row, col, steps = queue.popleft()
            
            if (row, col) == targetCell:
                return steps
            
            for direct in directions:
                xRow = row + direct[0]
                yCol = col + direct[1]
                
                if (xRow, yCol) not in visited and self.isValid(grid, xRow, yCol, numRows, numCols):
                    queue.append((xRow, yCol, steps + 1))
                    visited.add((xRow, yCol))
                    
        return -1