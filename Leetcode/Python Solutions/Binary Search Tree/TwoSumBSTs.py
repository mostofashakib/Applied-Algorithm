"""
LeetCode Problem: 1214. Two Sum BSTs
Link: https://leetcode.com/problems/two-sum-bsts/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N_1+N_2), where N_1 and N_2N
Space Complexity: O(N_1 +max(N_1,N_2))

Explanation: In this approach, we make use of the fact that the given tree is a Binary Search Tree.
Now, we know that the inorder traversal of a BST gives the nodes in ascending order.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        ListA = set()
        ListB = []
        
        if root1 is None and root2 is None: return False
        if root1 is None or root2 is None: return False
        
        def helperA(node):
            if node is None:
                return
            helperA(node.left)
            ListA.add(target-node.val)
            helperA(node.right)
            
        def helperB(node):
            if node is None:
                return
            helperB(node.left)
            ListB.append(node.val)
            helperB(node.right)
        
        helperA(root1)
        helperB(root2)
        
        for i in ListB:
            if i in ListA:
                return True
            
        return False