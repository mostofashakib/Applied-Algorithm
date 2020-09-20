"""
LeetCode Problem: 304. Range Sum Query 2D - Immutable
Link: https://leetcode.com/problems/range-sum-query-2d-immutable/
Video resources: https://www.youtube.com/watch?v=PwDqpOMwg6U
Language: Python
Written by: Mostofa Adib Shakib
"""

# Optimal Solution
# Time Complexity: O(n)
# Space Complexity: O(1)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0: return
        
        self.matrix = matrix
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        
        self.dp = [ [0 for i in range(columns+1)] for j in range(rows+1) ]
        
        for i in range(rows):
            for j in range(columns):
                self.dp[i+1][j+1] = self.matrix[i][j] + self.dp[i][j+1] + self.dp[i+1][j] - self.dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



# Brute Force
# Time Complexity: O(mn)
# Space Complexity: O(1)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        count = 0
        
        for row in range(row1, row2+1):
            for column in range(col1, col2+1):
                count += self.matrix[row][column]
        return count
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)