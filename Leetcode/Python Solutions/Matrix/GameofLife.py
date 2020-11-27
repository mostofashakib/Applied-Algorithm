"""
LeetCode Problem: 289. Game of Life
Link: https://leetcode.com/problems/game-of-life/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(M*N)
Space Complexity: O(M*N)

M = Number of rows
N = Number of columns
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        columns = len(board[0])

        # A helper function to check how many neighbouring cells are alive
        
        def checkNeighbours(board, row, column):
            cells = 0
            
            if column-1 >= 0 and board[row][column-1] == 1:
                cells += 1
            
            if column+1 < len(board[0]) and board[row][column+1] == 1:
                cells += 1
                
            if row-1 >= 0 and board[row-1][column] == 1:
                cells += 1
            
            if row+1 < len(board) and board[row+1][column] == 1:
                cells += 1
            
            if  row+1 < len(board) and column+1 < len(board[0]) and board[row+1][column+1] == 1:
                cells += 1
                
            if  row+1 < len(board) and column-1 >= 0 and board[row+1][column-1] == 1:
                cells += 1
                
            if row-1 >= 0 and column+1 < len(board[0]) and board[row-1][column+1] == 1:
                cells += 1
                
            if row-1 >= 0 and column-1 >= 0 and board[row-1][column-1] == 1:
                cells += 1
                
            return cells
        
        # Keeps a copy of the originalBoard
        originalBoard =  [[board[row][col] for col in range(columns)] for row in range(rows)]
                
        for row in range(rows):
            for column in range(columns):
                # Checks how many neighbouring alive cells does a particular cell has
                aliveCells = checkNeighbours(originalBoard, row, column)
                
                # Checks if a particular cell in the original board is alive               
                if originalBoard[row][column] == 1:
                    # If an alive cell has less than 2 or greater than 3 neighbouring alive cells then it dies
                    if aliveCells < 2 or aliveCells > 3:
                        board[row][column] = 0
                
                else:
                    # If a dead cell has exactly 3 neighbouring alive cells then it becomes alive
                    if aliveCells == 3:
                        board[row][column] = 1