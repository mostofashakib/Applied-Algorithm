"""
LeetCode Problem 257. Binary Tree Paths
Link: https://leetcode.com/problems/binary-tree-paths/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)

Time complexity : We visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes.
Space complexity : Linear space is needed for the call stack.

Algorithm:

1) If node is not NULL then 
     concatenate the string with the value of the node: 
            string =  string + node.val
2) If node is a leaf node then append the string to the result array
3) Else
    a) Recursively call the helper function on the left subtree
            helper(node.left, string)
    b) Recursively call the helper function on the right subtree
            helper(node.right, string)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helper(node, string):
            if not node: return
            
            string += str(node.val)
            
            if node.left == None and node.right == None:
                result.append(string)
                
            else:
                string += '->'
                helper(node.left, string)
                helper(node.right, string)
        
        result = []
        helper(root, '')
        
        return result