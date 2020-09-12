"""
LeetCode Problem: 37. Sudoku Solver
Link: https://leetcode.com/problems/sudoku-solver/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n*2^n)
Space Complexity: O(n)
"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # Returns the coordinates of the next available cell in the board
        def nextPositionToFill(board):
            row = len(board)
            column = len(board[0])
            
            for r in range(row):
                for c in range(column):
                    if board[r][c] == ".":
                        return r,c
            return -1, -1
        
        # Checks if the value placed is valid
        def isValid(board, row, column, value):
            
            rowOK = all([value != board[row][index] for index in range(len(board)) ])
            
            if rowOK:
                columnOK = all([value != board[index][column] for index in range(len(board[0]))])
                if columnOK:
                    box_x = 3 * (row//3)
                    box_y = 3 * (column//3)
                    
                    for r in range(box_x, box_x+3):
                        for c in range(box_y, box_y+3):
                            if board[r][c] == value:
                                return False               
                    return True
            return False
        
        # The main recursive method that solves the sudoku board
        def sudokuSolver(board, row, column):
            row, column = nextPositionToFill(board)
            
            if (row, column) == (-1, -1):
                return True
            
            for value in range(1, len(board)+1):
                if isValid(board, row, column, str(value)):
                    board[row][column] = str(value)
                    if sudokuSolver(board, row, column):
                        return True
                    board[row][column] = "."                            # Backtracking step
                    
            return False
                
        return sudokuSolver(board, 0, 0)