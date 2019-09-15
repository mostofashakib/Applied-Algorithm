"""
LeetCode Problem: 104. Maximum Depth of a Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root: return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1
    