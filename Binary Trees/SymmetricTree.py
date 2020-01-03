"""
LeetCode Problem: 101. Symmetric Tree
Link: https://leetcode.com/problems/symmetric-tree/
Language: Python
Written by: Mostofa Adib Shakib

Symmetric Tree:

A Tree is said to be symmetric if it is structurally symmetric and if the corresponding nodes have the same value.

Algorithm:

Pass two versions of the same tree and traverse. The Tree is symmetric if and only if
    1) The left child of Tree 1 is equal to the right child of Tree 2.
    2) The right child of Tree 1 is equal to the left child of Tree 2.

Time Complexity: O(n)
Space Complexity: O(h)     # height
"""

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)              # pass two versions of the same Tree

    def isMirror(self, root1, root2):
        if not root1 and not root2:                   # if the Tree is empty then it is Symmetric
            return True
        
        if root1 is not None and root2 is not None:     # traverse if both of the roots are present
            if root1.val == root2.val:                  # traverse if both of the corresponding nodes have the same value
                return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
        
        return False             # if any of the above conditions are not True then the Tree is not symmetric
