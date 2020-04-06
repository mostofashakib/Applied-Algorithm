"""
LeetCode Problem: 48. Rotate Image
Link: https://leetcode.com/problems/rotate-image/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity:  O(n)
Space Complexity: O(1)

"""

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])  

        # transpose matrix means swapping ith row with ith column
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        
        # reverse each row of the transposed matrix
        for i in range(n):
            matrix[i].reverse()