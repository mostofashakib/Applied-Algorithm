"""
LeetCode Problem: 59. Spiral Matrix II
Link: https://leetcode.com/problems/spiral-matrix-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        
        matrix = [ [i for i in range(j, j+n)] for j in range(1, n*n +1, n) ]
        rows, columns = n, n
        forwards, rights = 0, 0
        Rflag, cFlag = False, False
        i, j = 0, 0
        index = 1  # maximum number of traversals
        
        while index < n*n +1:
            # Top traversal
            
            if Rflag == False and cFlag == False:
                if j == columns-1:
                    cFlag = True
                    matrix[i][j] = index
                    forwards += 1   # We shrink the top bounds
                    i += 1          # To avoid duplications
                else:
                    matrix[i][j] = index
                    j += 1
            
            # Right traversal
            
            elif Rflag == False and cFlag == True:
                if i == rows - 1:
                    Rflag = True
                    matrix[i][j] = index
                    columns -= 1    # We shrink the right bounds
                    j -= 1          # To avoid duplications
                else:
                    matrix[i][j] = index
                    i += 1
            
            # Bottom traversal
            
            elif Rflag == True and cFlag == True:
                if j == rights:
                    cFlag = False
                    matrix[i][j] = index
                    rows -= 1       # We shrink the bottom bounds
                    i -= 1          # To avoid duplications
                else:
                    matrix[i][j] = index
                    j -= 1
            
            # Left traversal
            
            else:
                if i == forwards:
                    Rflag = False
                    matrix[i][j] = index
                    rights += 1     # We shrink the left bounds
                    j += 1          # To avoid duplications
                else:
                    matrix[i][j] = index
                    i -= 1
            
            index += 1
            
        return matrix