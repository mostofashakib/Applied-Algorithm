"""
LeetCode Problem: 129. Sum Root to Leaf Numbers
Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
Language: Python
Written by: Mostofa Adib Shakib

Leaf Node:

Both the left and right child is a Null Node

Algorithm:

1) Check if the node passed is a Null Node if so return from the recursive call
2) Concatenate the string with the value of the current Node.
3) If the current node is a leaf node then change the string to an integer and append it to the result array
4) If the current node is not a leaf node then recursively call both it's left and right subtree
5) return the sum of the result array

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = []
        
        def helper(node, string):
            nonlocal result
            
            if not node: return
            
            string += str(node.val)
            
            if not node.left and not node.right:
                result.append(int(string))
            else:
                helper(node.left, string)
                helper(node.right, string)
        
        helper(root, "")
        
        return sum(result)
