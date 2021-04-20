"""
LeetCode Problem: 114. Flatten Binary Tree to Linked List
Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def flatten(self, root: TreeNode) -> None:        
        if not root:
            return None
        
        while root:
            if root.left:
                rightmost = root.left
                
                while rightmost.right:
                    rightmost = rightmost.right
                    
                rightmost.right = root.right
                root.right = root.left
                root.left = None
            
            root = root.right