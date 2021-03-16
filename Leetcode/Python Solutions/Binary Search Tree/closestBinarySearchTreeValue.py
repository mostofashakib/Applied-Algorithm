"""
LeetCode Problem: 270. Closest Binary Search Tree Value
Link: https://leetcode.com/problems/closest-binary-search-tree-value/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return 0
        
        def dfs(node, target):
            nonlocal miniDiffVal
            nonlocal miniDiffKey
            
            if not node:
                return
            
            if miniDiffVal > abs(target-node.val):
                miniDiffVal = abs(target-node.val)
                miniDiffKey = node.val
                
            if node.val > target:
                return dfs(node.left, target)
            
            else:
                return dfs(node.right, target)
        
        miniDiffVal = float('inf')
        miniDiffKey = -1
        dfs(root, target)
        return miniDiffKey