"""
LeetCode Problem: 766. Toeplitz Matrix
Link: https://leetcode.com/problems/toeplitz-matrix/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Optimal Solution
# Time Complexity: O(M*N)
# Space Complexity: O(1) 

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        
        for r in range(rows):
            for c in range(columns):
                if r > 0 and c > 0 and matrix[r-1][c-1] != matrix[r][c]:
                    return False
        return True

# Brute Force
# Time Complexity: O(N^2)
# Space Complexity: O(N)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        temp = matrix[0][:-1]
        
        for r in range(1, rows):
            subArray = matrix[r]
            
            if subArray[1:] != temp:
                return False
            
            temp = subArray[:-1]
        
        return True