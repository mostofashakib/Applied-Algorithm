"""
LeetCode Problem 993. Cousins in Binary Tree
Link: https://leetcode.com/problems/cousins-in-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def depth(node, key, height, parent):
            if not node: return []
            
            if node.val == key: return [height, parent.val]
            
            return depth(node.left, key, height+1, node) or depth(node.right, key, height+1, node)
        
        x_info = depth(root, x, 0, root)
        y_info = depth(root, y, 0, root)
        
        return x_info[0] == y_info[0] and x_info[1] != y_info[1]