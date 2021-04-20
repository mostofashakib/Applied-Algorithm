"""
LeetCode Problem: 119. Pascals Triangle 2
Link: https://leetcode.com/problems/pascals-triangle-ii/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def getRow(self, rowIndex):
        def helper(row):
            return [ row[i]+row[i+1] for i in range(len(row)-1) ]
        
        if rowIndex == 0:
            return [1] 
        
        if rowIndex == 1:
            return [1 , 1]
        
        res = []
        res.append([1])
        res.append([1, 1])
        
        for i in range(2, (rowIndex+1)):
            res.append([1] + helper(res[i-1]) + [1])
            
        return res[rowIndex]