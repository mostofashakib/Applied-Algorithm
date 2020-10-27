"""
LeetCode Problem: 173. Binary Search Tree Iterator
Link: https://leetcode.com/problems/binary-search-tree-iterator/
Language: Python
Written by: Mostofa Adib Shakib

Time complexity : O(1)
Space complexity : O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        
        # Preorder traversal of a BST gives us an array sorted in an ascending order
        def preorderTraversal(node):
            if not node:
                return
                
            preorderTraversal(node.left)
            self.stack.append(node.val)
            preorderTraversal(node.right)
        
        preorderTraversal(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        # If the stack is not empty then pop off the first element from the end of the stack
        # Remember that the top-most element in the stack is the biggest number in the sorted array and the end-most element is the smallest
        if self.stack:
            return self.stack.pop(0)
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        # If the stack is not empty return True or else return False
        if self.stack:
            return True
        else:
            return False
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()