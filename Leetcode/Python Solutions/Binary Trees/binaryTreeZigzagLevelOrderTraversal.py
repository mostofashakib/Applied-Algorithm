"""
LeetCode Problem: 103. Binary Tree Zigzag Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        flag = False
        ans = []
        
        while queue:
            length = len(queue)
            currentLevel = []
            
            for i in range(length):
                node = queue.pop(0)
                currentLevel.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                
            if flag:
                ans.append(currentLevel[::-1])
                flag = False
            else:
                ans.append(currentLevel)
                flag = True
                
        return ans