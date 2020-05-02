"""
LeetCode Problem: 124. Binary Tree Maximum Path Sum
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(log n)
"""


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def max_gain(root):
            nonlocal max_sum                                # makes max_sum being accessed by the outer function
            if not root: return 0                           # leaf node
            
            left_gain = max(max_gain(root.left), 0)             # discards negative numbers
            right_gain = max(max_gain(root.right), 0)           # discards negative numbers
            
            new_path_gain = root.val + left_gain + right_gain   # finds the maximum sum of a given node
             
            max_sum = max(max_sum, new_path_gain)               # only updates if the new_path_gain is greater than the max_sum
            
            return root.val + max(left_gain, right_gain)        # this is used to keep recursing
        
        max_sum = float('-inf')                                 # initializes max_sum
        max_gain(root)
        
        return max_sum


# Solution 2

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        
        def helper(node):
            nonlocal ans
            
            if not node: return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            ans = max(ans, left + right + node.val)
            
            return max(0, node.val + max(left, right) )
        
        helper(root)
        
        return ans