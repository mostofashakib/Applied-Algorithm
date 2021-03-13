"""
LeetCode Problem: 230. Kth Smallest Element in a BST
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = []
        
        # Inorder traversal of a binary search tree gives us a sorted array
        def inOrder(node):
            if node:
                inOrder(node.left)
                
                ans.append(node.val)
                
                inOrder(node.right)
                
        inOrder(root)
        
        return ans[k-1]