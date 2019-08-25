"""

LeetCode Problem: 662. Maximum width of a binary tree.
Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

"""


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
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