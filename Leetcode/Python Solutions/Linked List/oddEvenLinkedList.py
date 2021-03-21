"""
LeetCode Problem: 328. Odd Even Linked List
Link: https://leetcode.com/problems/odd-even-linked-list/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummyEven = ListNode(0)
        dummyOdd = ListNode(0)
        tempOdd = dummyOdd              # Reference to the dummy node point to the odd indices
        tempEven = dummyEven            # Reference to the dummy node point to the even indices
        curr = head                     # Reference to the head of the linkedList
        flag = True                     # Boolen used to switch between iterating dummyEven and dummyOdd
        
        while curr:
            if flag:
                tempOdd.next = curr
                tempOdd = tempOdd.next
                flag = False
            else:
                tempEven.next = curr
                tempEven = tempEven.next
                flag = True
            
            curr = curr.next
        
        tempEven.next = None            # The last node should point to Null in order to avoid cycles
        tempOdd.next = dummyEven.next   # merge the two linkedLists togethers
        
        return dummyOdd.next