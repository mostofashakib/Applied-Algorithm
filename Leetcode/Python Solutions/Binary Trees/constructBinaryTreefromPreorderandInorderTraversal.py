"""
LeetCode Problem 105. Construct Binary Tree from Preorder and Inorder Traversal
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left, right):            
            if left > right:
                return None
            
            rootValue = queue.popleft()
            root = TreeNode(rootValue)
                        
            root.left = helper(left, hashMap[rootValue]-1)
            root.right = helper(hashMap[rootValue]+1, right)
            
            return root
        
        hashMap = {}
        queue = deque(preorder)
        
        for index, value in enumerate(inorder):
            hashMap[value] = index
            
        return helper(0, len(preorder)-1)