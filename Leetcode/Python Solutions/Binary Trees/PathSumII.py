"""
LeetCode Problem: 113. Path Sum II
Link: https://leetcode.com/problems/path-sum-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Approach 1: Depth First Traversal | Recursion | String

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        def helper(node, amount, string):
            if not node: return   # if not node then reture
            
            # substract the current node's value and concatenate the node's value with a string

            amount -= node.val
            string += str(node.val) + ','

            # only add the result if it's a leaf node and the remaining sum is 0 

            if node.left == None and node.right == None and amount == 0:
                string = string.split(',')
                result.append(string[:-1])
            else:
            	# recurse the left and right subtree
                helper(node.left, amount, string)
                helper(node.right, amount, string)
        
        # the result array stores the path        
        result = []
        helper(root, sum, '')
        return result

# Approach 2: Depth First Traversal | Recursion | Array

class Solution:
    
    def recurseTree(self, node, remainingSum, pathNodes, pathsList):
        if not node: return 
        
        # Add the current node to the path's list
        pathNodes.append(node.val)
        
        # Check if the current node is a leaf and also, if it
        # equals our remaining sum. If it does, we add the path to our list of paths
        if remainingSum == node.val and not node.left and not node.right:
            pathsList.append(list(pathNodes))
        else:    
            # Else, we will recurse on the left and the right children
            self.recurseTree(node.left, remainingSum - node.val, pathNodes, pathsList)
            self.recurseTree(node.right, remainingSum - node.val, pathNodes, pathsList)
            
        # We need to pop the node once we are done processing ALL of it's subtrees.
        pathNodes.pop()    
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pathsList = []
        self.recurseTree(root, sum, [], pathsList)
        return pathsList