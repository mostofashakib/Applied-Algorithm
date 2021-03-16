"""
LeetCode Problem: 723. Candy Crush
Link: https://leetcode.com/problems/candy-crush/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O((M * N)^2)
Space Complexity: O(N)
"""

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        crushed = False
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == 0: continue
                v = abs(board[i][j])
                
                # for vertical crush
                if i < R - 2 and v == abs(board[i+1][j]) == abs(board[i+2][j]):
                    board[i][j] = board[i+1][j] = board[i+2][j] = -v
                    crushed = True
                
                # for horizontal crush
                if j < C - 2 and v == abs(board[i][j+1]) == abs(board[i][j+2]):
                    board[i][j] = board[i][j+1] = board[i][j+2] = -v
                    crushed = True
        
        if crushed:
            
            for j in range(C):
                row_idx = R - 1
                
                # start assigning positive values to the bottom row idx
                for i in range(R-1, -1, -1):
                    if board[i][j] > 0:
                        board[row_idx][j] = board[i][j]
                        row_idx -= 1
                
                # all remaining rows from here on mark as 0
                while row_idx >= 0:
                    board[row_idx][j] = 0
                    row_idx -= 1
        
        return self.candyCrush(board) if crushed else board