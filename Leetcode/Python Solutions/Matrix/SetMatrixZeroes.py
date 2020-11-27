"""
LeetCode Problem: 73. Set Matrix Zeroes
Link: https://leetcode.com/problems/set-matrix-zeroes/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(M*N)
Space Complexity: O(M*N)

M: Number of rows
N: Number of columns
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # A helper function that sets all the cells in a particular row and column to 0
        def setRowColumn(matrix, row, column):
            for r in range(len(matrix)):
                matrix[r][column] = 0
            
            for c in range(len(matrix[0])):
                matrix[row][c] = 0
        
        rows = len(matrix)
        columns = len(matrix[0])
        
        # Creates a copy of the original matrix
        originalMatrix = [[matrix[row][col] for col in range(columns)] for row in range(rows)]
        
        for row in range(rows):
            for column in range(columns):
                # If any of the cell is 0 then set all the cells in that row and column to be 0
                if originalMatrix[row][column] == 0:
                    setRowColumn(matrix, row, column)