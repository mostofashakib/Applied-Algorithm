"""
LeetCode Problem: 445. Add Two Numbers II
Link: https://leetcode.com/problems/add-two-numbers-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        FirstNumber = ""
        SecondNumber = ""
        FirstPointer = l1
        SecondPointer = l2
        
        while FirstPointer:
            FirstNumber += str(FirstPointer.val)
            FirstPointer = FirstPointer.next
            
        while SecondPointer:
            SecondNumber += str(SecondPointer.val)
            SecondPointer = SecondPointer.next
            
        amount = int(FirstNumber) + int(SecondNumber)
        
        Pointer = ListNode()
        head = Pointer
        
        for i in str(amount):
            new_node = ListNode()
            new_node.val = int(i)
            Pointer.next = new_node
            Pointer = Pointer.next
            
        return head.next