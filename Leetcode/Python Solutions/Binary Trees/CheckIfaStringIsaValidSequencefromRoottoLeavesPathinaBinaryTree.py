"""
LeetCode LC 30 day challenge.Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
Link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/
Link: https://www.geeksforgeeks.org/check-root-leaf-path-given-sequence/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n) # recursive stack
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(node, arr, i, n):
            # null node
            if not node or i == n: return False
            
            # leaf node
            if not node.left and not node.right:
                if node.val == arr[i] and i == n-1:
                    return True
                return False
            
            return (i<n) and node.val == arr[i] and dfs(node.left, arr, i+1, n) or dfs(node.right, arr, i+1, n) 
            
        if not root:
            if len(arr) == 0:
                return True
        
        return dfs(root, arr, 0, len(arr))
            
            
        