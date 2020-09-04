"""
LeetCode Problem: 142. Linked List Cycle II
Link: https://leetcode.com/problems/linked-list-cycle-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.
        
        tortoise = head
        hare = head
        
        while True and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next if hare.next.next else hare.next
            if tortoise == hare:
                break
        
        if not hare.next:
            return None

        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        
        tortoise = head
        
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
            
        return tortoise