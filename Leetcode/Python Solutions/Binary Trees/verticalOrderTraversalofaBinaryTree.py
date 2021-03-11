"""
LeetCode Problem: 987. Vertical Order Traversal of a Binary Tree
Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        hashMap = defaultdict(list)
        minimumColumn  = 0
        maximumColumn = 0
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, column = queue.popleft()
            hashMap[column].append((row, node.val))
            
            if node.left:
                minimumColumn = min(minimumColumn, column-1)
                queue.append((node.left, row+1, column-1))
            
            if node.right:
                maximumColumn = max(maximumColumn, column+1)
                queue.append((node.right, row+1, column+1))
        
        result = []
        
        # sort first by 'row', then by 'value', in ascending order
        for i in range(minimumColumn, maximumColumn+1):
            temp = hashMap[i]
            result.append([val for row, val in sorted(temp)])
        
        return result