"""
LeetCode Problem 1578. Minimum Deletion Cost to Avoid Repeating Letters
Link: https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
Written by: Mostofa Adib Shakib
Language: Python

Time Complexity: O(N^2)
Space Complexity: O(N)
"""

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if not s:
            return 0
        
        i = 0
        longestSequence = 0
        minTotalCost = 0
        length = len(s)
        
        # Helper function to determine the minimum cost to delete letters in a sequence
        def minRangeSum(cost, i , j):            
            return sum(cost[i:j]) - max(cost[i:j])  
        
        while i < length:
            # Find the length of the longest continuous sequence
            while longestSequence + i + 1 < length and s[longestSequence + i + 1] == s[longestSequence + i]:
                longestSequence += 1
            
            # If there is a continuous sequence
            if longestSequence > 0:
                minTotalCost += minRangeSum(cost, i, i + longestSequence + 1)
                i = i + longestSequence + 1    # move the pointer after the sequence ends
                longestSequence = 0            # reset the count
            else:
                i += 1
            
        return minTotalCost