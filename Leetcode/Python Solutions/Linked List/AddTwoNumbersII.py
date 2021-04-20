"""
LeetCode Problem: 445. Add Two Numbers II
Link: https://leetcode.com/problems/add-two-numbers-ii/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find the length of both lists
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next 
            n1 += 1
        while curr2:
            curr2 = curr2.next 
            n2 += 1
            
        # parse both lists
        # and sum the corresponding positions 
        # without taking carry into account
        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3
        curr1, curr2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0
            
            if n1 > n2:
                val += curr1.val 
                curr1 = curr1.next 
                n1 -= 1
            elif n2 > n1:
                val += curr2.val 
                curr2 = curr2.next
                n2 -= 1
            else:
                val += curr1.val 
                val += curr2.val
                curr1 = curr1.next
                curr2 = curr2.next
                n1 -= 1
                n2 -= 1
                
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

        # take the carry into account
        # to have all elements to be less than 10
        # 10->10->3 --> 0->1->4 --> 4->1->0
        curr1, head = head, None
        carry = 0
        while curr1:
            # current sum and carry
            val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10
            
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the list
            curr1 = curr1.next
        
        # add the last carry
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head