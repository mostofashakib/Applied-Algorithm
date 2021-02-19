"""
LeetCode Problem: 138. Copy List with Random Pointer
Link: https://leetcode.com/problems/copy-list-with-random-pointer/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        
        curr = head
        hashmap = {}
        
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
            
        curr = head
        
        while curr:
            if curr.next:
                hashmap[curr].next = hashmap[curr.next]
                
            if curr.random:
                hashmap[curr].random = hashmap[curr.random]
                
            curr = curr.next
            
        return hashmap[head]

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head:
            return None
        curr = head
        
        while curr:
            nxt = curr.next
            new = Node(curr.val, nxt, None)
            new.next = curr.next
            curr.next = new
            curr = curr.next.next
            
        curr = head
        
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        curr = head
        nxt = head.next
        
        while curr.next:
            temp = curr.next
            curr.next = curr.next.next
            curr = temp
        return nxt