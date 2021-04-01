"""
LeetCode Problem: 98. Validate Binary Search Tree
Link: https://leetcode.com/problems/validate-binary-search-tree/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

# Approach One: Using Range

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if root.right is None and root.left is None:
            return True
        
        def helper(node, left, right):
            if node is None:
                return True
            
            if left != None and node.val <= left:
                return False
            
            if right != None and node.val >= right:
                return False
            
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)
        
        return helper(root, None, None)

# Approach Two: Using InOrder Traversal

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if not root.right and not root.left:
            return True
        
        array = []
        
        def inOrder(node):
            if not node:
                return
            
            inOrder(node.left)
            array.append(node.val)
            inOrder(node.right)
        
        inOrder(root)
        
        for i in range(1, len(array)):
            if array[i-1] >= array[i]:
                return False

        return True
