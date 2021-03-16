"""
LeetCode Problem: 1290. Convert Binary Number in a Linked List to Integer
Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0        
        
        while head:
            count = 2*count + head.val
            head = head.next
            
        return count