"""
LeetCode Problem: 117. Populating Next Right Pointers in Each Node II
Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = [root]
        
        while queue:
            # Note the size of the queue
            size = len(queue)
            
            # Iterate over all the nodes on the current level
            for i in range(size):
                
                # Pop a node from the front of the queue
                node = queue.pop(0)
                
                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only 
                # don't establish next pointers beyond the end of a level
                if i < size - 1:
                    node.next = queue[0]
                
                # Add the children, if any, to the back of the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root