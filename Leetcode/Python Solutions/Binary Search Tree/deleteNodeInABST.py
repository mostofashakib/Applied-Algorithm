"""
LeetCode Problem: 450. Delete Node in a BST
Link: https://leetcode.com/problems/delete-node-in-a-bst/
Further Reading: https://leetcode.com/problems/delete-node-in-a-bst/discuss/821420/Python-O(h)-solution-explained
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        else:
            if not root.left and not root.right:
                return None
            
            elif root.left and not root.right:
                return root.left
            
            elif root.right and not root.left:
                return root.right
            
            else:
                temp = root.right
                
                while temp.left:
                    temp = temp.left
                    
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
        
        return root