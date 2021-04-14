"""
LeetCode Problem: 662. Maximum width of a binary tree.
Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

In a balanced binary tree for the node at level "L"

    The left child will be at the index: 2 * L
    The right child will be at the index: 2 * L + 1
"""

# Approach 1

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        queue = [(root, 0)]
        count = 0
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                node, level = queue.pop(0)
                
                if node.left:
                    queue.append((node.left, 2 * level))
                
                if node.right:
                    queue.append((node.right, 2 *level + 1))
            
            if not queue:
                break
                            
            leftBound = queue[0]
            rightBound = queue[-1]
            count = max(count, rightBound[1] - leftBound[1] + 1)
        
        return count

# Approach 2

class Solution(object):
    def widthOfBinaryTree(self, root):
        queue = [(root, 0, 0)]
        curr_depth = ans = left = 0
        
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2 +1) )
                if curr_depth != depth:
                    curr_depth = depth
                    left = pos
                ans = max(pos - left +1, ans)
        return ans