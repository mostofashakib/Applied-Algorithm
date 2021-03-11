"""
LeetCode Problem:965. Univalued Binary Tree
Link: https://leetcode.com/problems/univalued-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

Two versions of the solution

Version 1(Recursive using DFS):

In this version of the solution we use a dfs helper method to compare every node in the true. If the value of every node is not equal to the 
root node we return False. This method is faster as it doesn't iterative every node.

Version 2(Iteratively using In-Order traversal):

In this version of the solution we use a stack. We push all the left child of a node into the stack up until we reach a Null node.
If we reach a Null node and the stack is not empty then we pop an element from the stack and and compare it's value with the root node
if they are equal then we append it's right child to the stack or else we return False. This method is a bit slower as we are iterating over
all the left child of a node before comparing it's value with the root node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# Version 1(Recursion using DFS)

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(root,val):
            if not root: return True
            return root.val == val and dfs(root.left,val) and dfs(root.right,val)
        
        return dfs(root,root.val)
    
    
# Version 2(Iteratively using In-Order traversal)

class Solution(object):
def isUnivalTree(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    if not root: return True
    
    curr = root
    stack = []
    
    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            if root.val != curr.val:
                return False
            curr = curr.right
        else:
            break
    return True