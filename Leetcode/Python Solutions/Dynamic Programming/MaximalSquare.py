"""
LeetCode Problem: 221. Maximal Square
Link: https://leetcode.com/problems/maximal-square/
Language: Python
Written by: Mostofa Adib Shakib

Explanation:

If during the recursion you find you're solving the same sub-problem repeatedly ("overlapping sub-problems") - that's the first hint that its DP. Next,
if you find that the optimal answer for the current sub-problem is formed from the optimal answer for the overlapping sub-problems,
you now have found the optimal sub-structure. Its DP for sure. Typically problems involving finding the "longest/shortest/largest/smallest/maximal" of
something have the optimal-substructure. For example if the shortest distance from A to D is A->B->C->D, then it follows that the shortest distance
from B to D is B->C->D. At first sight, this problem requires a DFS traversal - a dead giveaway that we need recursion. And it also wants you to find
the largest square. So you'd go to the first 1 and ask it, "Hey, what's the largest square of 1s that begins with you?". To calculate that it needs to
know the largest squares its adjacent cells can begin. So, it'll ask the same question to its adjacent cells which will in turn will ask their adjacent
cells and so on... The cell that began the question will deduce that the largest square that begins with it is
1 + the minimum of all the values its adjacent cells returned.
You'd then ask the same question to every 1 you find in the grid and keep track of the global maximum.
In doing so, you'll notice that the recursion causes many cells to be asked the same question again and again (overlapping sub-problems)-
so you'd use memoization.

"""


"""
Dynamic Programming
Time Complexity: O(m*n)  
Space Complexity: O(m*n)
M = Number of row
N = Number of column
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix[0]) == 0: return 0
        
        ans = 0
        
        dp = [ [0 for i in range(len(matrix[0]))] for j in range(len(matrix)) ]
        
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if row == 0 or column == 0:
                    dp[row][column] = int(matrix[row][column])
                elif matrix[row][column] == '1':
                    dp[row][column] = int(matrix[row][column]) + min(dp[row-1][column], dp[row][column-1], dp[row-1][column-1])
                
                ans = max(ans, dp[row][column])
                    
        return ans*ans


"""
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