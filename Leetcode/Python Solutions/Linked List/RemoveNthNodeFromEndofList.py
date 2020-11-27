"""
LeetCode Problem: 19. Remove Nth Node From End of List
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = head
        length = 0
        
        # This calculates the length of the linkedList chain for example if a chain has 5 nodes then the length is 4
        while dummyHead.next:
            length += 1
            dummyHead = dummyHead.next
        
        # This takes care of the edge cases for example if there is only one node in the linkedList chain then we return None
        # If the node to be removed is the first node in the linkedList chain then we just move the position of head
        if length == 0:
            return None
        elif length-n+1 == 0:
            return head.next
        
        count = 0                                   # Keeps track of the running length
        
        previousNode = None                         # Initialize a Previouse Node
        currentNode = head                          # Initialize a copy of head
        
        # Keep traversing up until we get to the node that is just behind the node we want to remove
        while count < length-n+1:
            previousNode = currentNode
            currentNode = currentNode.next
            count += 1
        
        previousNode.next = currentNode.next        # This delete the nth node from the linkedList chain 
        
        return head