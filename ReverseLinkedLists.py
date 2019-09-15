"""
LeetCode Problem: 206. Reverse a Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Language: Python
Written by: Mostofa Adib Shakib
"""

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev