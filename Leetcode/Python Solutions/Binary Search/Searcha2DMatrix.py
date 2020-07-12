"""
LeetCode Problem 240. Search a 2D Matrix II

Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
Written by: Mostofa Adib Shakib
Language: Python

m = rows
n = coumns

idx = n*m -1  # index of the last element

row = idx // n
col = idx % n.

Time Complexity: O(n*m)
Space complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False
