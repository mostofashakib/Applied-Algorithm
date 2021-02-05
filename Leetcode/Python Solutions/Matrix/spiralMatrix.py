"""
LeetCode Problem: 54. Spiral Matrix
Link: https://leetcode.com/problems/spiral-matrix/
Written by: Mostofa Adib Shakib
Language: Python

n is the total number of cells in the matrix

Time Complexity: O(n)
Space Complexity: O(n)
"""

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
        