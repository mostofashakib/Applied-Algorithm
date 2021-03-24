"""
LeetCode Problem: 85. Maximal Rectangle
Link: https://leetcode.com/problems/maximal-rectangle/
Language: Python
Written by: Mostofa Adib Shakib

This question is similar to the Largest Rectangle in Histogram question on Leetcode 

Time Complexity: O(R*C)
Space Complexity: O(N)
"""

class Solution:
    def largestAreaInAHistogram(self, heights):
        heights.append(0)
        ans = 0
        stack = [-1]
        length = len(heights)
        
        for i in range(length):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height*width)
            stack.append(i)
        return ans
        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        columns = len(matrix[0])
        rows = len(matrix)
        
        for r in range(rows):
            for c in range(columns):
                if r == 0:
                    matrix[r][c] = int(matrix[r][c])
                else:
                    if matrix[r][c] == "0":
                        matrix[r][c] = 0
                    else:
                        matrix[r][c] = matrix[r-1][c] + int(matrix[r][c])
        
        ans = 0
        for r in range(rows):
            currentAns = self.largestAreaInAHistogram(matrix[r])
            ans = max(ans, currentAns)
        
        return ans