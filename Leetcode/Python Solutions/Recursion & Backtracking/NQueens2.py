"""
LeetCode Problem: 52. N-Queens II
Link: https://leetcode.com/problems/n-queens-ii/
Github: https://github.com/mostofashakib/Applied-Algorithm 
Language: Python
Written by: Mostofa Adib Shakib


Two programming conceptions:

1) Constrained  Programming: Put restrictions after each queen placement.
    One puts a queen on the board and that immediately excludes one column,
    one row and two diagonals for the further queens placement.

2) Backtracking: Puts several queens on the board so that they don't attack each other. But the combination chosen is not the optimal one and there is no place for the next queen.
    What to do? To backtrack.That means to come back, to change the position of the previously placed queen and try to proceed again.
    If that would not work either, backtrack again.

Algorithm:

If all rows are filled up row == N
That means that we find out one more solution.

Else
    Start from the first row = 0.
    Iterate over the columns and try to put a queen in each column.

    If square (row, column) is not under attack

        Place the queen in (row, column) square.
        Exclude one row, one column and two diagonals from further consideration.

    Proceed to place further queens backtrack(row + 1).
    Now backtrack : remove the queen from (row, column) square.

Time Complexity: O(n!)
Space Complexity: O(N)
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        board = [ [False for i in range(n)] for i in range(n)  ]
        self.solve(0, n, board, result)
        return len(result)
        
    def solve(self, row, n, board, result):
        # base condition

        if row == n:    # if all the queens are safely placed then we have found a solution
            result.append(1)
        else:
            for col in range(n): # loop over all the cols of a given row
                if self.isValid(row, col, board) == True:   # check if a queen is getting attacked or not
                    board[row][col] = True   # mark the cell as True meaning a queen can be safely placed here
                    self.solve(row+1, n, board, result)   # recursively calls the next row for the next queen to be placed
                    board[row][col] = False #backtrack if a queen cannot be placed in the board
        

    def isValid(self, row, col, board):
        # checking if there is a queen directly above the row from a given row-coloumn

        for r in  range(row):
            if board[r][col] == True:
                return False
        
        # checking if there is a queen attacking from the left diagonal

        r = row -1
        c = col -1

        while r >= 0 and c >= 0:
            if board[r][c] == True:
                return False
            r -= 1
            c -= 1
        
        # checking if there is a queen attacking from the right diagonal

        r = row -1
        c = col +1

        while r >= 0 and c < len(board):
            if board[r][c] == True:
                return False
            r -= 1
            c += 1

        # if the queen is not getting attacked from any other queens from above then return True

        return True