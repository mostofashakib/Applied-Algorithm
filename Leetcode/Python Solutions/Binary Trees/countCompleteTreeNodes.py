"""
LeetCode Problem: 222. Count Complete Tree Nodes
Link: https://leetcode.com/problems/count-complete-tree-nodes/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Optimal Solution
# Time Complexity: O(Log^2N)
# Space Complexity: O(N)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        leftInterval = 1
        leftNode = root.left
        
        # Find the depth of the left most node
        while leftNode:
            leftNode = leftNode.left
            leftInterval += 1
        
        rightInterval = 1
        rightNode = root.right
        
        # Find the depth of the right most node
        while rightNode:
            rightNode = rightNode.right
            rightInterval += 1
        
        # The node is a perfect binary tree
        if rightInterval == leftInterval:
            return (2**rightInterval) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# Brute Force Solution
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        count = 0
        
        def preOrder(node):
            nonlocal count
            
            if not node:
                return
            
            count += 1
            
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        
        return count