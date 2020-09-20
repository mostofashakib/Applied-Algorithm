"""
LeetCode Problem: 1289. Minimum Falling Path Sum II
Link: https://leetcode.com/problems/minimum-falling-path-sum-ii/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Optimal Solution
# Time Complexity: O(m*n)
# Space Complexity: O(1)

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1, len(A)):
            # picks the smallest two element from the previous row
            r = heapq.nsmallest(2, A[i - 1])
            
            for j in range(len(A[0])):
                # cannot pick adjacent elements
                if A[i - 1][j] == r[0]:
                    A[i][j] += r[1]
                else:
                    A[i][j] += r[0]
                
        return min(A[-1])                   # returns the smallest sum possible

# Brute Force
# Time Complexity: O(m*n*n!)
# Space Complexity: O(n)


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr: return 0
        
        def helper(row, column, temp):
            if row == n:
                result.append(temp.copy())
            else:
                temp.append(arr[row][column])
                
                for i in range(len(arr[0])):
                    if i != column:
                        helper(row+1, i, temp)
                        
                temp.pop()
                        
        result = []
        n = len(arr)
        
        for i in range(len(arr[0])):
            helper(0, i, [])
            
        minimum = float('inf')
        
        for i in result:
            minimum = min(minimum, sum(i))
            
        return minimum