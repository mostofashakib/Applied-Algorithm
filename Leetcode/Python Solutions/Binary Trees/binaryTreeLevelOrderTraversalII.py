"""
LeetCode Problem: 107. Binary Tree Level Order Traversal II
Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # Edge case
        if not root:
            return []
        
        queue = [root]
        result = []
        
        while queue:
            nextLevel = []
            
            for i in range(len(queue)):
                node = queue.pop(0)
                
                nextLevel.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            result.append(nextLevel)
            
        return result[::-1]