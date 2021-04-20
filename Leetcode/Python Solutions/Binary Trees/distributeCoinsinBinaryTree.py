"""
LeetCode Problem: 979. Distribute Coins in Binary Tree
Link: https://leetcode.com/problems/distribute-coins-in-binary-tree/
Further Reading: https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)

Explanation:

1)  Root asks the left subtree, how much do you need or you've got extra? I'll give that/take it away to/from you via
    our direct edge, and pass it to right child, and if something remains, I'll take it.
2)  Same question is asked to the right child.
3)  Answer will be the sum of values(absolute) returned after the asked questions from the left(Left) and right(Right).
    But what should the root return to its parent? It will return that how much does "his tree" need/has extra. That will
    be the signed sum of its Left+Right (question's answer) + same question asked to current root node.
"""

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        
        def helper(node):
            if not node:
                return 0
        
            leftChild  = helper(node.left)
            rightChild = helper(node.right)

            self.moves += abs(leftChild) + abs(rightChild)

            return node.val + leftChild + rightChild - 1
        
        helper(root)
        return self.moves