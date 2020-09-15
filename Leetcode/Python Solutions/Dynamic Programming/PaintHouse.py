"""
LeetCode Problem: 256. Paint House
Link: https://leetcode.com/problems/paint-house/
Written by: Mostofa Adib Shakib
Language: Python
"""

# Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        
        n = len(costs)
        
        for i in range(1, n):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        
        return min(costs[n-1][0], costs[n-1][1], costs[n-1][2])



# Recursion + Memoization
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        
        n = len(costs) - 1
        
        @lru_cache(maxsize=None)
        def helper(firstColor, secondColor, thirdColor, index):
            if index < 0:
                return 0
            if firstColor:
                return costs[index][0] + min(helper(False, True, False, index-1), helper(False, False, True, index-1))
            if secondColor:
                # 
                return costs[index][1] + min(helper(True, False, False, index-1), helper(False, False, True, index-1))
            if thirdColor:
                return costs[index][2] + min(helper(True, False, False, index-1), helper(False, True, False, index-1))
            
        return min(helper(True, False, False, n), helper(False, True, False, n), helper(False, False, True, n))