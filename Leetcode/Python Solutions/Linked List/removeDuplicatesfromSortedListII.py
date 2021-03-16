"""
LeetCode Problem: 82. Remove Duplicates from Sorted List II
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node 
        # before the sublist of duplicates
        pred = sentinel
        
        while head:
            # if it's a beginning of duplicates sublist 
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next 
            # otherwise, move predecessor
            else:
                pred = pred.next 
                
            # move forward
            head = head.next
            
        return sentinel.next