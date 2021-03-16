"""
LeetCode Problem: 513. Find Bottom Left Tree Value
Link: https://leetcode.com/problems/find-bottom-left-tree-value/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        ans = []
        
        while queue:
            size = len(queue)
            temp = []
            
            for i in range(size):
                node = queue.pop(0)
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            ans.append(temp)
        
        return ans[-1][0]