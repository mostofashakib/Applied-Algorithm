"""
LeetCode Problem: 112. Path Sum
Link: https://leetcode.com/problems/path-sum/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(log n)

"""

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False                                 # if the tree is empty
        
        if not root.left and not root.right:                      # if it's a leaf node
            return sum == root.val
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)      # traverse both of the node's subtrees