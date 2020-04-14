"""
LeetCode Problem 543. Diameter of Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        
        def depth_first_search(node):
            if not node: return 0                  # base case for leaf node
            left  = depth_first_search(node.left)
            right = depth_first_search(node.right)
            self.ans = max(self.ans, left+right)    # maximum overall annswer
            return 1 + max(left, right)             # maximum height of the left & right subtree
            
        depth_first_search(root)
        return self.ans