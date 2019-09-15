"""
LeetCode Problem: 226. Invert a Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root is None: return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root