"""
LeetCode Problem: 106. Construct Binary Tree from Inorder and Postorder Traversal
Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hashMap = defaultdict(int)
        
        for index, key in enumerate(inorder):
            hashMap[key] = index
        
        def dfsHelper(left, right):
            if left > right:
                return None
            
            root = TreeNode(postorder.pop())
            index = hashMap[root.val]
            
            root.right = dfsHelper(index+1, right)
            root.left = dfsHelper(left, index-1)
            
            return root
        
        return dfsHelper(0, len(inorder) - 1)