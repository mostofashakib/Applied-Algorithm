"""
LeetCode Problem: 285. Inorder Successor in BST
Link: https://leetcode.com/problems/inorder-successor-in-bst/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Optimal Solution
# Time Complexity: 
#    Average Case: O(logN)
#    Worst Case: O(N)
# Space Complexity: O(1)

class Solution:        
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor

# Brute Force
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def binarySearch(self, array, target):
        minimumDiff = float('inf')
        left = 0
        right = len(array) - 1
        
        while left <= right:
            mid = (left+right)//2
            
            if array[mid] == target:
                return array[mid]
            
            elif array[mid] < target:
                left = mid + 1
            else:
                minimumDiff = min(minimumDiff, array[mid])
                right -= 1
        
        if minimumDiff == float('inf'):
            return -1
        else:
            return minimumDiff
        
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        array = []
        hashMap = {}
        
        def preOrderHelper(root):
            if not root:
                return

            preOrderHelper(root.left)
            hashMap[root.val] = root
            array.append(root.val)
            preOrderHelper(root.right)
        
        preOrderHelper(root)
        
        result = self.binarySearch(array, p.val+1)
        
        return hashMap[result] if result != -1 else None