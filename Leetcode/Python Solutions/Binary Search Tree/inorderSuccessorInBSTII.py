"""
LeetCode Problem: 510. Inorder Successor in BST II
Link: https://leetcode.com/problems/inorder-successor-in-bst-ii/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Optimal Solution
# Time Complexity: 
#    Average Case: O(logN)
#    Worst Case: O(N)
# Space Complexity: O(1)

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # If a right subtree exisits then the successor will be the node with the minimum val in the right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # We walk up until we encounter a node that has the next greatest value from the given node 
        while node.parent and node.parent.val < node.val:
            node = node.parent
            
        return node.parent

# Brute Force
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        array = []
        hashMap = {}
        
        def inOrderTraversal(node):
            if not node:
                return
            
            inOrderTraversal(node.left)
            hashMap[node.val] = node
            array.append(node.val)
            inOrderTraversal(node.right)
        
        root = node
        
        while root.parent is not None:
            root = root.parent
                
        inOrderTraversal(root)
    
        for num in array:
            if num > node.val:
                return hashMap[num]
        
        return None