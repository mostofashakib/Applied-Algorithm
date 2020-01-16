"""
LeetCode Problem: 236. Lowest Common Ancestor of a Binary Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

Side note: A node can also be it's own ancestor

The root is the lowest common ancestor if and only if the following two conditions are true:
    1) If the nodes are in different immediate subtrees of the root.
    2) If one of the nodes is the root.

Algorithm:

We solve the problem using a bottom-up fashion.

1) If the root is None return None
2) If the root value is equal to the value of either one of the nodes return root
3) Recurse the left subtree
4) Recurse the right subtree
5) If both the nodes are found in the two subtrees then return root.
6) If both the nodes are in the left subtree then the return the LCA of the left subtree
7) If both the nodes are in the right subtree then the return the LCA of the right subtree

Time Complexity: O(n)
Space Complexity: O(h)   # height

"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root: return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left = lowestCommonAncestor(root.left, p, q)
        right = lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right
