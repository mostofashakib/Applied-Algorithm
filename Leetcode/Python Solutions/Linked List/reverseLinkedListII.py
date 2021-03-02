"""
LeetCode Problem: 92. Reverse Linked List II
Link: https://leetcode.com/problems/reverse-linked-list-ii/
Language: Python
Written by: Mostofa Adib Shakib
"""

# Iterative Link Reversal
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next  or left == right:
            return head
        
        prev = None
        curr = head
        
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
        
        connection = prev
        tail = curr
        
        while right > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            right -= 1
            
        if connection:
            connection.next = prev
        else:
            head = prev
            
        tail.next = curr
        
        return head


# Brute Force
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next  or left == right:
            return head
        
        count = 0
        startingNode = head
        
        while count < left-1:
            startingNode = startingNode.next
            count += 1
        
        endingNode = startingNode
        
        while count < right-1:
            endingNode = endingNode.next
            count += 1
            
        reverseValues = []
        curr = startingNode
        i = 0
        
        while i < (right-left + 1):
            reverseValues.append(curr.val)
            curr = curr.next
            i += 1
        
        while len(reverseValues) > 0:
            startingNode.val = reverseValues.pop()
            startingNode = startingNode.next
        
        return head