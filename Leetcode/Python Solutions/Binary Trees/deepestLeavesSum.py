"""
LeetCode Problem: 1302. Deepest Leaves Sum
Link: https://leetcode.com/problems/deepest-leaves-sum/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        ans = 0
        
        while queue:
            length = len(queue)
            ans = 0
            
            for i in range(length):
                node = queue.pop(0)
                ans += node.val
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return ans