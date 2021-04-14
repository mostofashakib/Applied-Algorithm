"""
LeetCode Problem: 77. Combinations
Link: https://leetcode.com/problems/combinations/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(kCN)
Space Complexity: O(kCN)
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def recursiveHelper(idx, path):
            # If the combination is done
            if len(path) == k:
                result.append(path.copy())
                return
            
            for i in range(idx, n):
                # Add i into the current combination
                path.append(i+1)
                # Use next integers to complete the combination
                recursiveHelper(i+1, path)
                # Backtrack
                path.pop()
        
        for i in range(n):
            recursiveHelper(i+1, [i+1])
        
        return result