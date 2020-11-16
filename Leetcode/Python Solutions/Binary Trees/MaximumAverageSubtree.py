"""
LeetCode Problem: 1120. Maximum Average Subtree
Link: https://leetcode.com/problems/maximum-average-subtree/
Language: Python
Written by: Mostofa Adib Shakib

Time Compplexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        def depthFirstSearch(node):
            # If we encounter a null node
            if not node:
                return [0, 0, 0]        # currentSum, numberOfNodes, maxAverage
            
            # Get the maximum average possible for the left & right subtree
            leftSubTree = depthFirstSearch(node.left)
            rightSubTree = depthFirstSearch(node.right)
            
            # Calculate the currentSum, numberOfNodes, and maxAverage
            
            currentSum =  leftSubTree[0] + rightSubTree[0] + node.val
            numberOfNodes = leftSubTree[1] + rightSubTree[1] + 1
            maxAverage = max(leftSubTree[2], rightSubTree[2], currentSum/numberOfNodes)
            
            # Return the currentSum, numberOfNodes, and maxAverage for each subtree
            
            return [currentSum, numberOfNodes, maxAverage]
        
        return depthFirstSearch(root)[2]