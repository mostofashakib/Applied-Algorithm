"""
LeetCode Problem: 61. Rotate List
Link: hhttps://leetcode.com/problems/rotate-list/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(1)
"""

# Approach 1

class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        
        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head

# Approach 2

class Solution:
    def swapHelper(self, head, index, length):
        i = length - index
        prev = None
        curr = head
        
        while index > 0:
            prev = curr
            curr = curr.next
            index -= 1
        
        prev.next = None
        startNode = curr
                
        if curr.next is None:
            curr.next = head
            return startNode
        
        while i > 0:
            curr = curr.next
            i -= 1
            
            if curr.next is None:
                curr.next = head
                break
            
        return startNode
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        curr = head
        length = 0
        endNode = None
        
        while curr:
            if curr.next is None:
                endNode = curr
            curr = curr.next
            length += 1
            
        if length == 1 or k % length == 0:
            return head
            
        if k > length:
            actualSwaps = k % length
            index = length - actualSwaps
            return self.swapHelper(head, index, length)
        else:
            return self.swapHelper(head, length-k, length)