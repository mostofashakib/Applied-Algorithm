"""
LeetCode Problem: 216. Combination Sum III
Link: https://leetcode.com/problems/combination-sum-iii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O( (9!⋅K)/(9−K)! )
Space Complexity: O(K)
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def recursiveHelper(index, path, target):
            if target < 0 or len(path) > k:
                return
            
            if target == 0 and len(path) == k:
                result.append(path.copy())
                return
            
            for i in range(index, 10):
                path.append(i)
                recursiveHelper(i+1, path, target - i)
                path.pop()
        
        recursiveHelper(1, [], n)
        return result