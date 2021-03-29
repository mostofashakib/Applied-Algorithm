"""
LeetCode Problem: 63. Unique Paths II
Link: https://leetcode.com/problems/unique-paths-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(M*N)
Space Complexity: O(1)
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        rowFlag = False
        columnFlag = False
        
        # fixing the rows
        for r in range(1, rows):
            if obstacleGrid[r][0] == 0 and not rowFlag:
                obstacleGrid[r][0] = 1
            
            elif obstacleGrid[r][0] == 1:
                obstacleGrid[r][0] = 0
                rowFlag = True
                
            if rowFlag:
                obstacleGrid[r][0] = 0
        
        # fixing the columns
        for c in range(columns):
            if obstacleGrid[0][c] == 0 and not columnFlag:
                obstacleGrid[0][c] = 1
            
            elif obstacleGrid[0][c] == 1:
                obstacleGrid[0][c] = 0
                columnFlag = True
                
            if columnFlag:
                obstacleGrid[0][c] = 0
        
        # fixing the other grids
        for r in range(1, rows):
            for c in range(1, columns):
                if obstacleGrid[r][c] == 0:
                    obstacleGrid[r][c] = 1
                else:
                    obstacleGrid[r][c] = 0
        
        # calculating the unique number of ways
        for r in range(1, rows):
            for c in range(1, columns):
                if obstacleGrid[r][c] != 0:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
                                    
        return obstacleGrid[-1][-1]