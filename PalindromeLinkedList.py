"""
234 leetcode. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
"""


"""

Edge case: If there is no linkedlist we return True.

We try to find the midpoint of the linkedlist by running two pointers through the linkedlist at different speed.
We use a stack and store all the values from the second half of the linkedlist. we compare the value from the top of the stack 
with the values from the first half of the linkedlist. If the stack is empty and all the values match then we return true
else we return false and end the program.

"""

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:return True
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        stack = []
        while slow:
            stack.append(slow.val)
            slow = slow.next
        while head and stack:
            val = stack.pop()
            if val != head.val: return False
            head = head.next
        return True