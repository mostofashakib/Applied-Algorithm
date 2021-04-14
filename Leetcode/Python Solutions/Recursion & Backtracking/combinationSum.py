"""
LeetCode Problem: 39. Combination Sum
Link: https://leetcode.com/problems/combination-sum/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N^(T/M + 1) )
Space Complexity: O(T/M)
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        
        def recursiveHelper(index, path, target):
            if target < 0:
                return
            
            if target == 0:
                result.append(path.copy())
                return
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                recursiveHelper(i, path, target - candidates[i])
                path.pop()
        
        recursiveHelper(0, [], target)
        return result