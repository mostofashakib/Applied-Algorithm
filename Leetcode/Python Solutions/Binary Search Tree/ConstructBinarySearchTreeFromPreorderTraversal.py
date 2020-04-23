"""

LeetCode Problem: 1008. Construct Binary Search Tree from Preorder Traversal
Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
Language: Python
Written by: Mostofa Adib Shakib

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative solution
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return
        if len(preorder) == 1: return TreeNode(preorder[0])
                
        root = TreeNode(preorder[0])
        pointer = root
                
        for i in preorder[1:]:
            while True:
                if i < pointer.val:
                    if pointer.left is not None:
                        pointer = pointer.left
                    else:
                        pointer.left = TreeNode(i)
                        pointer = root
                        break
                else:
                    if pointer.right is not None:
                        pointer = pointer.right
                    else:
                        pointer.right = TreeNode(i)
                        pointer = root
                        break
        return root
        
# Recursive solution
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return
        
        length = len(preorder)
        
        root = TreeNode(preorder.pop(0))
        
        LSides = []
        RSides = []
        
        for i in preorder:
            if i > root.val:
                RSides.append(i)
            else:
                LSides.append(i)
        
        root.left = self.bstFromPreorder(LSides)
        root.right = self.bstFromPreorder(RSides)
        
        return root
