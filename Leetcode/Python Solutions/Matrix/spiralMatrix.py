"""
LeetCode Problem: 54. Spiral Matrix
Link: https://leetcode.com/problems/spiral-matrix/
Written by: Mostofa Adib Shakib
Language: Python

n is the total number of cells in the matrix

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Approach 1

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        result = []
        direction = 0
        
        while top <= bottom and left <= right:
            if direction == 0:                
                for i in range(left, right+1):
                    result.append(matrix[top][i])
                top += 1
                
            elif direction == 1:
                for i in range(top, bottom+1):
                    result.append(matrix[i][right])
                right -= 1
            
            elif direction == 2:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
                
            direction = (direction + 1) % 4
            
        return result


# Approach 2

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        rows, columns = len(matrix), len(matrix[0])
        forwards, rights = 0, 0
        Rflag, cFlag = False, False
        i, j = 0, 0
        index = len(matrix) * len(matrix[0])   # maximum number of traversals
        
        while index > 0:
            # Top traversal
            
            if Rflag == False and cFlag == False:
                if j == columns-1:
                    cFlag = True
                    result.append(matrix[i][j])
                    forwards += 1   # We shrink the top bounds
                    i += 1          # To avoid duplications
                else:
                    result.append(matrix[i][j])
                    j += 1
            
            # Right traversal
            
            elif Rflag == False and cFlag == True:
                if i == rows - 1:
                    Rflag = True
                    result.append(matrix[i][j])
                    columns -= 1    # We shrink the right bounds
                    j -= 1          # To avoid duplications
                else:
                    result.append(matrix[i][j])
                    i += 1
            
            # Bottom traversal
            
            elif Rflag == True and cFlag == True:
                if j == rights:
                    cFlag = False
                    result.append(matrix[i][j])
                    rows -= 1       # We shrink the bottom bounds
                    i -= 1          # To avoid duplications
                else:
                    result.append(matrix[i][j])
                    j -= 1
            
            # Left traversal
            
            else:
                if i == forwards:
                    Rflag = False
                    result.append(matrix[i][j])
                    rights += 1     # We shrink the left bounds
                    j += 1          # To avoid duplications
                else:
                    result.append(matrix[i][j])
                    i -= 1
            
            index -= 1
            
        return result
        