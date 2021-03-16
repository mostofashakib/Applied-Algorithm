"""
LeetCode Problem: 333. Largest BST Subtree
Link: https://leetcode.com/problems/largest-bst-subtree/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        def postOrder(root):
            nonlocal result
            
            if root is None:
                return True, float('inf'), float('-inf'), 0
            
            isLeftBst, leftMin, leftMax, leftSize = postOrder(root.left)
            isRightBst, rightMin, rightMax, rightSize = postOrder(root.right)
            
            # Subtree is a Binary Search Tree
            if isLeftBst and isRightBst and root.val > leftMax and root.val < rightMin:
                result = max(result, leftSize + rightSize +1)           # Leftsize + rightsize + node itself
                leftMin = min(root.val, leftMin)                        # Lowest of subtree)
                rightMax = max(root.val, rightMax)                      # Maxest of subtree)
                return True, leftMin, rightMax, leftSize + rightSize +1
            # Subtree is not a Binary Search Tree
            else:
                return False, float('inf'), float('-inf'), 0
        
        result = 0
        postOrder(root)
        return result