"""
LeetCode Problem: 118. Pascal's Triangle
Link: https://leetcode.com/problems/pascals-triangle/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        result = [[1],[1,1]]
        
        for i in range(2, numRows):
            currentRow = [1]
            lastRow = result[-1]
            
            for j in range(len(lastRow) -1):
                currentRow.append(lastRow[j] + lastRow[j+1])
            
            result.append(currentRow + [1])
            
        return result