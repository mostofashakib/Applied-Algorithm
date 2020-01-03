"""
LeetCode Problem: 221. Maximal Square
Link: https://leetcode.com/problems/maximal-square/
Language: Python
Written by: Mostofa Adib Shakib

Dynamic Programming: Recursion + Top-Down Method(Memoization)
Time Complexity: O(m*n)  
Space Complexity: O(m*n)
M = Number of row
N = Number of column
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def SquareFinder(matrix, row, column, memo):                         # helper method recursively finds the number of squares
            if row >= len(matrix) or column >= len(matrix[0]): return 0      # restricting matrix bounds
            if matrix[row][column] == '0': memo[row][column] = 0             # if 0 then it cannot be a complete square
            if memo[row][column] != -1: return memo[row][column]             # if value is preciously computed
            else:
                memo[row][column] = min(SquareFinder(matrix, row+1, column, memo), SquareFinder(matrix, row, column+1, memo), SquareFinder(matrix, row+1, column+1, memo)) + 1                      # recursively checks to see how many squares can be found
                
            return memo[row][column]         # returns the value
         
        maxS = 0                              # a counter that tracks the maximum squares seen so far
        memo = [ [-1 for i in range(len(matrix[0]))] for j in range(len(matrix)) ]      # memo matrix
        
        for i in range(len(matrix)):            # traverses the matrix looking for the maximum square
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    maxS = max(maxS, SquareFinder(matrix, i, j, memo) )
                    
        return maxS * maxS  # returns the maximal square