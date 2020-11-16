"""
LeetCode Problem: 199. Binary Tree Right Side View
Link: https://leetcode.com/problems/binary-tree-right-side-view/
Language: Python
Written by: Mostofa Adib Shakib

Time Compplexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # Return an empty array if the root is a null node
        if not root:
            return []
        
        queue = [root]                                      # Initialize a queue
        result = []                                         # Initialize a result array
        
        # Keep looping as long as the queue is not empty
        while queue:
            count = len(queue)                              # Count how many nodes are in the current level
            
            # Process all the nodes that are in the same level
            while count > 0:
                
                currentNode = queue.pop(0)
                
                # Append the value of the right-most node in each level
                if count == 1:
                    result.append(currentNode.val)
                
                # Append the left child to the queue if it is not null                    
                if currentNode.left: 
                    queue.append(currentNode.left)
                
                # Append the right child to the queue if it is not null
                if currentNode.right: 
                    queue.append(currentNode.right) 

                count -= 1
                
        return result