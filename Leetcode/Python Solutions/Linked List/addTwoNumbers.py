"""
LeetCode Problem: 2. Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(max(M,N))
Space Complexity: O(max(M,N))
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        listOneNode = l1
        listTwoNode = l2
        carry = 0
        curr = dummyHead
        
        while listOneNode != None or listTwoNode != None:
            listOneVal = listOneNode.val if listOneNode != None else 0
            listTwoVal = listTwoNode.val if listTwoNode != None else 0
            
            total = listOneVal + listTwoVal + carry
            carry = total // 10
            lastDigit = total % 10
            
            curr.next = ListNode(lastDigit)
            curr = curr.next
            
            if listOneNode:
                listOneNode = listOneNode.next
            
            if listTwoNode:
                listTwoNode = listTwoNode.next
                
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummyHead.next