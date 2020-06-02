"""
LeetCode Problem: 437. Path Sum III
Link: https://leetcode.com/problems/path-sum-iii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n^2)
Space Complexity: O(n)   # linear space for call stack
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def helper(node, amount, arr):
            nonlocal count   # in order to access count in the main function
            
            if not node: return
            
            arr.append(node.val)  # append the value to the list
                
            helper(node.left, amount, arr)  # recursively call the left subtree
            helper(node.right, amount, arr) # recursively call the right subtree
            
            temp = 0
            for i in range(len(arr)-1, -1,-1):  # traverse backwards since it's not necesary to include the root
                temp += arr[i]
                if temp == amount:
                    count += 1
            
            arr.pop(len(arr)-1)  # pop off the last element from the list after reaching the leaf node
        
        count = 0
        helper(root, sum, [])
        return count`