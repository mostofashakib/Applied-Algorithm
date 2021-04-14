"""
LeetCode Problem: 1315. Sum of Nodes with Even-Valued Grandparent
Link: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        
        def dfsHelper(current, parent, grandParent):
            if not current:
                return
            
            if grandParent != None and grandParent.val % 2 == 0:
                self.total += current.val
            
            dfsHelper(current.left, current, parent)
            dfsHelper(current.right, current, parent)
        
        dfsHelper(root, None, None)
        return self.total