"""
LeetCode Problem: 111. Minimum Depth of Binary Tree
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # Edge Case
        if not root:
            return 0
        
        # A helper function that calculates the minimum depth
        def dfsHelper(node):
            # return maximum for null node
            if not node:
                return float('inf')
            
            # Return 1 if leaf node
            if not node.right and not node.left:
                return 1
            
            return 1 + min(dfsHelper(node.left), dfsHelper(node.right))
        
        return dfsHelper(root)