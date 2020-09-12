"""
LeetCode Problem: 36. Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Brute Force
# Time Complexity: O(1)
# Space Complexity: O(n)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board[0])                                     # Calculates the length of the row
        column = len(board)                                     # Calculates the length of the column
        
        # A helper method to check a specific row is valid
        def checkRow(row):
            visited = set()
            
            for c in board[row]:
                if c == '.':
                    continue
                elif c not in visited:
                    visited.add(c)
                else:
                    return False
            return True
        
        # A helper method to check a specific column is valid
        def checkColumn(column):
            visited = set()
            
            for i in range(row):
                if board[i][column] == ".":
                    continue
                elif board[i][column] not in visited:
                    visited.add(board[i][column])
                else:
                    return False
            return True
        
        # A helper method to check a specific grid is valid
        def checkGrid(startRow, endRow, startColumn, endColumn):
            visited = set()
            
            for r in range(startRow, endRow):
                for c in range(startColumn, endColumn):
                    if board[r][c] == '.':
                        continue
                    elif board[r][c] not in visited:
                        visited.add(board[r][c])
                    else:
                        return False
            return True
            
        for r in range(row):
            if not checkRow(r):
                return False
            
        for c in range(column):
            if not checkColumn(c):
                return False
            
        for r in range(0,9,3):
            for c in range(0,9,3):
                if not checkGrid(r, r+3, c, c+3):
                    return False
                
        return True