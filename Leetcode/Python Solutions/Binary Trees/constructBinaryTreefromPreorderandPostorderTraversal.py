"""
LeetCode Problem: 889. Construct Binary Tree from Preorder and Postorder Traversal
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
            
        def dfsHelper(pre, post):
            if not pre:
                return None
        
            if len(pre) == 1:
                return TreeNode(post.pop())
        
            node = TreeNode(post.pop())
            idx = pre.index(post[-1])
        
            node.right = dfsHelper(pre[idx:], post)
            node.left = dfsHelper(pre[1:idx], post)
            
            return node
        
        return dfsHelper(pre, post)