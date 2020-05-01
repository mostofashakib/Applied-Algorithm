"""
LeetCode Problem: 653. Two Sum IV - Input is a BSTs
Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)

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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        
        def helper(node):
            if node is None:
                return
            helper(node.left)
            nums.append(node.val)
            helper(node.right)
                
        helper(root)
            
        FirstPointer = 0
        LastPointer = len(nums) - 1

        while FirstPointer < LastPointer:
            if nums[FirstPointer ] + nums[LastPointer] == k:
                return True
            elif nums[FirstPointer ] + nums[LastPointer] > k:
                LastPointer -= 1
            else:
                FirstPointer += 1
        return False