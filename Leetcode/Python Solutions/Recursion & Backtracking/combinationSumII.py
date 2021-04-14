"""
LeetCode Problem: 40. Combination Sum II
Link: https://leetcode.com/problems/combination-sum-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(2^N)
Space Complexity: O(N)
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result = []
        
        def recursiveHelper(index, path, target):
            if target < 0:
                return
            
            if target == 0:
                result.append(path.copy())
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                    
                path.append(candidates[i])
                recursiveHelper(i+1, path, target - candidates[i])
                path.pop()
        
        recursiveHelper(0, [], target)
        return result