"""
LeetCode Problem: 430. Flatten a Multilevel Doubly Linked List
Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head:
            n_stack = []        
            curr_node = head
            
            while curr_node:
                if curr_node.next:                      # Push the "next" (if there's a "next") first.
                    n_stack.append(curr_node.next)
                if curr_node.child:                     # Then push the "child" (if there's a child), 
                    n_stack.append(curr_node.child)     # so that the "stack" would pop the immediate "child" 
                    curr_node.child = None              # before any previous encountered "next".
                if n_stack:                             # It will "recurse" down and bubble back up eventually.
                    next_node = n_stack.pop()           # Unless it has traversed through all the nodes,
                    curr_node.next = next_node          # there's always some node left in the stack to pop.     
                    next_node.prev = curr_node          # Simply link up with whatever comes from the stack.
                curr_node = curr_node.next              # To the next node, or None if there's no more
                
        return head