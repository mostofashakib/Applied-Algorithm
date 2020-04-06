"""
LeetCode Problem: 23. Merge K Sorted Linked Lists
Link: https://leetcode.com/problems/merge-k-sorted-lists/
Language: Python
Written by: Mostofa Adib Shakib

N nodes in the final linked list.
k is the number of linked lists.

Time Complexity: O(N logk)
Space Complexity: O(k)
"""

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:  return None   # if the list is empty
        head = point = ListNode(0)   # The initial node 0 is a dummy reference.

        q = PriorityQueue()          # creates an instance of a priority queue

        for l in lists:              # puts all the first element from each sorted linked list into a priority queue
            if l:
                q.put((l.val, l))

        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next         # checks if a given sorted linked list still has a node
            if node:
                q.put((node.val, node))
                
        return head.next
    

# don't need to worry about this.

ListNode.__eq__ = lambda self, other: self.val == other.val
ListNode.__lt__ = lambda self, other: self.val < other.val
