"""
LeetCode Problem: 733. Flood Fill
Link: https://leetcode.com/problems/flood-fill/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity : O(N)
Space complexity : O(N)
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(image, row, col, color, newColor):
            if row < 0 or col < 0 or row > len(image)-1 or col > len(image[0])-1:
                return
            elif image[row][col] != color:
                return
            elif image[row][col] == color:
                image[row][col] = newColor
                dfs(image, row, col-1, color, newColor)
                dfs(image, row, col+1, color, newColor)
                dfs(image, row+1, col, color, newColor)
                dfs(image, row-1, col, color, newColor)
        
        color = image[sr][sc]
        
        if color != newColor:
            dfs(image, sr, sc, image[sr][sc], newColor)
        
        return image