"""
LeetCode Problem 240. Search a 2D Matrix II

Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
Written by: Mostofa Adib Shakib
Language: Python

Search space reduction Algorithm:

First, we initialize a (row, col)(row,col) pointer to the bottom-left of the matrix.
Then, until we find target and return true, we do the following:
    => If the currently-pointed-to value is larger than target we can move one row "up".
    => Otherwise, if the currently-pointed-to value is smaller than target, we can move one column "right".
It is not too tricky to see why doing this will never prune the correct answer; because the rows are sorted from left-to-right, we know that every value to the right of the current value is larger.
Therefore, if the current value is already larger than target, we know that every value to its right will also be too large.
A very similar argument can be made for the columns, so this manner of search will always find target in the matrix (if it is present).

Time Complexity: O(n + m)
Space complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height-1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False


# Binary Search
# Time Complexity: O(n log n)
# Space complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        def BinarySearch(arr, target):
            low = 0
            high = len(arr) -1
            
            while low <= high:
                mid = (low+high)//2
                
                if arr[mid] == target: return True
                
                elif arr[mid] > target:
                    high = mid - 1
                
                else:
                    low = mid + 1
        
        if not matrix: return False      # edge case
        
        row = len(matrix)                # length of row
        column = len(matrix[0])          # length of column
        
        for i in range(row):
            if BinarySearch(matrix[i], target) == True:
                return True
        
        return False                    # return False if the target cannot be found in the matrix

# Brute Force
# Time complexity: O(nm)   n = row; m = column
# Space complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix: return False     # edge case
        
        row = len(matrix)               # length of row
        column = len(matrix[0])         # length of column
        
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == target:
                    return True
                
        return False                    # return False if the target cannot be found in the matrix
