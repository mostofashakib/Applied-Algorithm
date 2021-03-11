"""
LeetCode Problem: 314. Binary Tree Vertical Order Traversal
Link: https://leetcode.com/problems/binary-tree-vertical-order-traversal/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        hashMap = {}
        min_column = 0     # Keeps track of the minimum idx possible
        max_column = 0     # Keeps track of the maximum idx possible
        queue = [(root, 0)]
        
        while queue:
            node, count = queue.pop(0)
            
            if count not in hashMap:
                hashMap[count] = [node.val]
            else:
                hashMap[count].append(node.val)
            
            if node.left:
                queue.append((node.left, count-1))
                min_column = min(min_column, count-1)
            
            if node.right:
                queue.append((node.right, count+1))
                max_column = max(max_column, count+1)
        
        result = []
        
        for idx in range(min_column, max_column+1):
            result.append(hashMap[idx])
        
        return result

