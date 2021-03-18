"""
LeetCode Problem: 86. Partition List
Link: https://leetcode.com/problems/partition-list/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Optimal Solution
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next

# Brute-Force Solution
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lessThanX = []
        greaterThanX = []
        curr = head
        
        while curr:
            if curr.val < x:
                lessThanX.append(curr.val)
            else:
                greaterThanX.append(curr.val)
            
            curr = curr.next
            
        curr = head
        
        while curr and lessThanX:
            node = lessThanX.pop(0)
            curr.val = node
            curr = curr.next
        
        while curr and greaterThanX:
            node = greaterThanX.pop(0)
            curr.val = node
            curr = curr.next
        
        return head