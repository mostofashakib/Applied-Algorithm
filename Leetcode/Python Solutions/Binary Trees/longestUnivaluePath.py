"""
LeetCode Problem: 687. Longest Univalue Path
Link: https://leetcode.com/problems/longest-univalue-path/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root or (not root.left and not root.right):
            return 0
        
        self.ans = 0
        
        def dfs(node):
            if not node or (not node.left and not node.right):
                return 0
            
            leftSubTree = dfs(node.left)
            rightSubTree = dfs(node.right)
            leftCount = 0
            rightCount = 0
            
            # count of the longest path on the left subtree
            if node.left and node.val == node.left.val:
                leftCount = leftSubTree + 1
            
            # count of the longest path on the right subtree
            if node.right and node.val == node.right.val:
                rightCount = rightSubTree + 1
                
            self.ans = max(self.ans, leftCount+rightCount)
            
            return max(leftCount, rightCount)
            
        dfs(root)
        return self.ans