"""
LeetCode Problem: 110. Balanced Binary Tree
Link: https://leetcode.com/problems/balanced-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

Concept:
A tree is said to be height balanced if the height difference
between the left and right subtree is at most 1.

Algorithm:
    Traverse the tree and keep track of the height difference of each subtree
    If the height difference is greater than 1 then return False else True.

Time Complexity: O(n)
Space Complexity: O(h)     # height
"""

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:          # if the tree is empty return True
            return True
        
        if self.maxDepth(root) < 0: 
            return False
        return True
    
    def maxDepth(self, root):
        if not root:        # if there is no Node then the maximum depth is 0
            return 0
        
        left = self.maxDepth(root.left)        # calculates the height of the left subtree
        right = self.maxDepth(root.right)      # calculates the height of the right subtree
        
        if left == -1 or right == -1:          # checks if the any of subtrees is height imbalanced
            return -1
        
        if abs(left - right) > 1:              # checks if the tree is height imbalanced
            return -1
        
        return max(left, right) + 1            # go to next depth so increment it by 1