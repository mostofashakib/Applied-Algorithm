"""

LeetCode Problem: 958. Check Completeness of Binary Tree
Link: https://leetcode.com/problems/check-completeness-of-a-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

"""


import collections

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        queue = collections.deque()
        queue.append(root)
        flag = False
        
        while queue:
            curr = queue.popleft()
            if curr is None:
                flag = True
            else:
                if flag is True:
                    return False
                queue.append(curr.left)
                queue.append(curr.right)
        return True