"""
LeetCode Problem #545. Boundary of Binary Tree
Link: https://leetcode.com/problems/boundary-of-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n) # recursive stack
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        # Finds all the nodes in the Left boundary
        def helperLeft(node):
            # Makes sure the node is not a leaf node or is not a null node
            if not node or not node.left and not node.right: return
            
            array.append(node.val)
            # Recurse to the right subtree only if the left subtree is not present
            if node.left:
                helperLeft(node.left)
            else:
                helperLeft(node.right)

        # Finds all the leaf nodes
        def helperLeaf(node):
            if not node: return
            
            # Makes sure the node is a leaf node and is not the root
            if node != root and not node.left and not node.right:
                array.append(node.val)
              
            if node.left: helperLeaf(node.left)                         # Recurse to the left subtree if present  
            if node.right: helperLeaf(node.right)                       # Recurse to the right subtree if present
        
        # Finds all the nodes in the Right boundary
        def helperRight(node):
            # Makes sure the node is not a leaf node or is not a null node
            if not node or not node.left and not node.right: return

            # Recurse to the left subtree only if the right subtree is not present
            if node.right:
                helperRight(node.right) 
            else:
                helperRight(node.left)
                
            array.append(node.val)
        
        # Edge cases

        if not root: return []
        if not root.left and not root.right: return [root.val]
        
        array = [root.val]
        
        helperLeft(root.left)
        helperLeaf(root)
        helperRight(root.right)

        return array